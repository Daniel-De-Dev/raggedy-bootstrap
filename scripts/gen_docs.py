#!/usr/bin/env python3
import os
import sys
import argparse
from typing import Any
import yaml
import glob

# Configuration
STRUCTS_DIR = "docs/structs/uefi"
OUT_DIR = "docs/uefi"
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
    """
    type_name = type_name.strip()

    # Pointers
    if type_name.endswith("*"):
        if "UINTN" not in structs:
            log_error(f"pointer type '{type_name}' used, but 'UINTN' is not defined.")
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

    return (0, 1)


def main():
    parser = argparse.ArgumentParser(description="UEFI Documentation Generator")
    parser.add_argument(
        "--check", action="store_true", help="Verify docs are up-to-date"
    )
    args = parser.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)
    yaml_files = glob.glob(os.path.join(STRUCTS_DIR, "*.yaml"))

    structs: dict[str, Any] = {}
    for filepath in yaml_files:
        with open(filepath, "r") as file:
            data = yaml.safe_load(file)
            if "size" in data and data["size"] == "NATIVE_WORD_SIZE":
                data["size"] = NATIVE_WORD_SIZE
            if "name" in data:
                structs[data["name"]] = data

    known_types = set(structs.keys())
    failure = False

    for name, data in structs.items():
        ref_link = data.get("reference_link")
        if not ref_link:
            log_error(f"'{name}' is missing the required 'reference_link' field.")
            failure = True
            continue

        md: list[str] = []
        md.append("---\n")
        md.append(f"uefi_version: {data.get('uefi_version', '2.11')}\n")
        md.append(f"architecture: {TARGET_ARCH_BITS}\n")
        md.append("---\n\n")
        md.append(
            "<!-- THIS FILE IS AUTO-GENERATED FROM YAML DATA. DO NOT EDIT DIRECTLY! -->\n\n"
        )
        md.append(f"# [{name}]({ref_link})\n\n")

        if "note" in data:
            md.append(f"**Note:** {data['note']}\n\n")

        if "fields" not in data and "size" in data:
            size, align = get_type_info(name, structs)
            md.append(f"**Primitive Type**\n\n")
            md.append(f"- **Size**: `{size}` bytes\n")
            md.append(f"- **Alignment**: `{align}` bytes\n")
        else:
            md.append(
                "| Offset (Dec) | Offset (Hex) | Type | Name | Size | Padding |\n"
            )
            md.append("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
            off = 0
            for field in data.get("fields", []):
                fname, ftype = field.get("name", "Unknown"), field.get(
                    "type", "Unknown"
                )
                sz, al = get_type_info(ftype, structs)
                pad = (al - (off % al)) % al
                fsz, fpad = field.get("size", sz), field.get("padding", pad)
                base = ftype.split("[")[0].replace("*", "").strip()
                dtype = (
                    f"[`{base}`]({base}.md){ftype[len(base):]}"
                    if base in known_types
                    else f"`{ftype}`"
                )

                if base not in known_types and base != "VOID":
                    log_warning(f"type '{base}' referenced in '{name}' is not defined.")

                md.append(
                    f"| {off} | `0x{off:02X}` | {dtype} | `{fname}` | {fsz} | {fpad} |\n"
                )
                off += fsz + fpad

        full_md = "".join(md)
        md_path = os.path.join(OUT_DIR, f"{name}.md")

        if args.check:
            if not os.path.exists(md_path):
                log_error(f"missing doc: {md_path}")
                failure = True
            else:
                with open(md_path, "r") as f:
                    if f.read() != full_md:
                        log_error(f"stale doc: {md_path}")
                        failure = True
        else:
            with open(md_path, "w") as f:
                f.write(full_md)

    if failure:
        sys.exit(1)
    elif args.check:
        log_info("all documentation is synchronized.")


if __name__ == "__main__":
    main()
