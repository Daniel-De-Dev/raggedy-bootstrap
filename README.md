# Raggedy Bootstrap

A bare-metal, self-hosting compiler chain from scratch. Targets RISC-V 64-bit
(RV64G) under the UEFI environment.

## Documentation

I've tried to keep good Documentation for the project. Please see
[`docs/README.md`](/docs/README.md)

## Getting Started

To enter the development environment:

```bash
nix develop
```

This will load all necessary dependencies, including QEMU for RISC-V, Python 3
with PyYAML, and the OVMF UEFI firmware.

## Development Workflow

### Emulator

To run the project in QEMU:

```bash
boot-riscv
```

This script:

1.  Creates a writable UEFI variable store (`_vars.fd`).
2.  Maps the `bootdir` directory as a virtual FAT drive.
3.  Boots the RISC-V Virt machine into UEFI.

Ensure your binary is located at `bootdir/EFI/BOOT/BOOTRISCV64.EFI` for UEFI to
find it automatically.

### Documentation

Due to needing to write manual machine code at the start, a simple doc generator
for UEFI structs was created. This way offsets and navigation between
definitions can easily be found.

The UEFI data structures are maintained as YAML files in `docs/structs/uefi/`.
To generate the Markdown documentation:

```bash
python3 scripts/gen_docs.py
```

This script calculates offsets and padding based on the standard 64-bit C ABI
automatically.

### Quality Control

The project uses `treefmt` via Nix to ensure consistent formatting across Nix,
Python, YAML, and Markdown.

- **Format everything**: `nix fmt`
- **Verify project integrity**: `nix flake check`

The `flake check` command verifies that:

1.  All files are correctly formatted.
2.  The generated Markdown documentation is perfectly synchronized with the YAML
    definitions (using `gen_docs.py --check`).

## Project Structure

- `docs/structs/uefi/`: Source YAML definitions for UEFI types.
- `docs/uefi/`: Generated Markdown documentation.
- `scripts/`: Internal toolchain scripts.
- `bootdir/`: The virtual disk content for the emulator.
- `seed.hx0`: The source of the stage-0 hex compiler.
