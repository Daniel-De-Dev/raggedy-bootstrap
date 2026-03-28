#!/usr/bin/env python3
import os
import sys
from typing import Any
import yaml
import glob

# TODO: Define github action to assert nix fmt and also some way to check
# if docs are up-to-date at each commit

STRUCTS_DIR = "docs/structs/uefi"
OUT_DIR = "docs/uefi"

# Configuration
TARGET_ARCH_BITS = 64
NATIVE_WORD_SIZE = TARGET_ARCH_BITS // 8


# Standardized Output Formatting
def log_error(msg: str) -> None:
    print(f"\033[1;31merror:\033[0m {msg}", file=sys.stderr)


def log_warning(msg: str) -> None:
    print(f"\033[1;33mwarning:\033[0m {msg}", file=sys.stderr)


def log_info(msg: str) -> None:
    print(f"\033[1;32minfo:\033[0m {msg}")


def get_type_info(type_name: str, structs: dict[str, Any]) -> tuple[int, int]:
    """
    Returns (size, alignment) in bytes for a given type.
    Resolves everything dynamically from the loaded YAML files.
    """
    type_name = type_name.strip()

    # Pointers
    # A pointer's size depends on the architecture. In UEFI, it's same as UINTN.
    if type_name.endswith("*"):
        if "UINTN" not in structs:
            log_error(
                f"pointer type '{type_name}' used, but 'UINTN' is not defined. Please create UINTN.yaml."
            )
            return (0, 1)
        return get_type_info("UINTN", structs)

    # Fixed-size Arrays
    if "[" in type_name and type_name.endswith("]"):
        base_type, count_str = type_name.split("[")
        count = int(count_str[:-1])
        base_size, base_align = get_type_info(base_type, structs)
        return (base_size * count, base_align)

    # Dynamic Lookup
    if type_name in structs:
        struct_def = structs[type_name]

        # Primitive Definition
        if "fields" not in struct_def and "size" in struct_def:
            size = struct_def["size"]
            # Default alignment to size if not explicitly provided
            align = struct_def.get("alignment", size)
            return (size, align)

        # Compound Struct Definition
        max_align = 1
        current_offset = 0
        for field in struct_def.get("fields", []):
            f_type = field.get("type")
            if not f_type:
                continue

            f_size, f_align = get_type_info(f_type, structs)

            # Manual override if size is explicitly set in the field
            f_size = field.get("size", f_size)

            # Calculate alignment padding
            calc_pad = (f_align - (current_offset % f_align)) % f_align
            pad = field.get("padding", calc_pad)

            max_align = max(max_align, f_align)
            current_offset += pad + f_size

        # Tail padding so the struct overall aligns properly if placed in an array
        tail_pad = (max_align - (current_offset % max_align)) % max_align
        return (current_offset + tail_pad, max_align)

    # Fallback for unknown types
    log_warning(f"unknown type '{type_name}'. Defaulting to size 0.")
    return (0, 1)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    yaml_files = glob.glob(os.path.join(STRUCTS_DIR, "*.yaml"))

    # Load all structs and primitives
    structs: dict[str, Any] = {}
    for filepath in yaml_files:
        with open(filepath, "r") as file:
            data = yaml.safe_load(file)

            # Substitute architecture-dependent constants on load
            if "size" in data and data["size"] == "NATIVE_WORD_SIZE":
                data["size"] = NATIVE_WORD_SIZE
            if "name" in data:
                structs[data["name"]] = data

    known_types = set(structs.keys())
    generated_count = 0

    # Generate the Markdown files
    for name, data in structs.items():
        ref_link = data.get("reference_link")
        if not ref_link:
            log_error(
                f"'{name}' is missing the required 'reference_link' field. Skipping..."
            )
            continue

        md_path = os.path.join(OUT_DIR, f"{name}.md")

        with open(md_path, "w") as f:
            # Metadata
            f.write("---\n")
            f.write(f"uefi_version: {data.get('uefi_version', '2.11')}\n")
            f.write(f"architecture: {TARGET_ARCH_BITS}\n")
            f.write("---\n\n")

            f.write(
                "<!-- THIS FILE IS AUTO-GENERATED FROM YAML DATA. DO NOT EDIT DIRECTLY! -->\n\n"
            )

            # Header
            f.write(f"# [{name}]({ref_link})\n\n")

            # Note/Comment
            if "note" in data:
                f.write(f"**Note:** {data['note']}\n\n")

            # Check if this is a Primitive or a Compound Struct
            if "fields" not in data and "size" in data:
                # Primitive
                size = data["size"]
                align = data.get("alignment", size)
                f.write(f"**Primitive Type**\n\n")
                f.write(f"- **Size**: `{size}` bytes\n")
                f.write(f"- **Alignment**: `{align}` bytes\n")
            else:
                # Struct
                f.write(
                    "| Offset (Dec) | Offset (Hex) | Type | Name | Size | Padding |\n"
                )
                f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")

                current_offset = 0

                # Calculate and write rows
                for field in data.get("fields", []):
                    fname = field.get("name", "Unknown")
                    ftype = field.get("type", "Unknown")

                    # Auto-calculate size and required padding based on ABI alignment
                    calc_size, calc_align = get_type_info(ftype, structs)
                    calc_pad = (calc_align - (current_offset % calc_align)) % calc_align

                    # Allow YAML overrides
                    fsize = field.get("size", calc_size)
                    fpad = field.get("padding", calc_pad)

                    # Auto-link types
                    base_type = ftype.split("[")[0].replace("*", "").strip()
                    if base_type in known_types:
                        display_type = f"[`{base_type}`]({base_type}.md)"
                        display_type = ftype.replace(
                            base_type, display_type
                        )  # restore * or []
                    else:
                        display_type = f"`{ftype}`"
                        log_warning(
                            f"type '{base_type}' referenced in '{name}' is not defined. Consider creating docs/structs/uefi/{base_type}.yaml"
                        )

                    dec_off = current_offset
                    hex_off = f"`0x{current_offset:02X}`"

                    f.write(
                        f"| {dec_off} | {hex_off} | {display_type} | `{fname}` | {fsize} | {fpad} |\n"
                    )

                    current_offset += fsize + fpad

        generated_count += 1

    log_info(
        f"successfully generated {generated_count} documentation files (Targeting {TARGET_ARCH_BITS}-bit architecture) in '{OUT_DIR}/'"
    )


if __name__ == "__main__":
    main()
