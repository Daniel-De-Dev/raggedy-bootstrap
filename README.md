# Raggedy Bootstrap

A bare-metal, self-hosting compiler chain from scratch. Targets RISC-V 64-bit in
UEFI.

I've tried to keep good Documentation for the project. Please see
[`docs/README.md`](/docs/README.md)

## Getting Started

To enter the development environment:

```bash
nix develop
```

This will load all necessary dependencies.

## Development Workflow

### Emulator

To run the project in QEMU:

```bash
boot-riscv
```

Note: Ensure your binary is located at `bootdir/EFI/BOOT/BOOTRISCV64.EFI` for
UEFI to find it automatically, or launch it trough the UEFI shell

### Documentation

Due to needing to write manual machine code, a simple doc generator for UEFI
structs was created. This way offsets and navigation between definitions can
easily be found.

The UEFI data structures are maintained as YAML files in `docs/structs/uefi/`.
To generate the Markdown documentation:

```bash
python3 scripts/gen_docs.py
```

### Quality Control

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
