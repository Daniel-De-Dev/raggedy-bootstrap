# Raggedy Bootstrap

A bare-metal, self-hosting compiler chain from scratch. Targets RISC-V 64-bit
(RV64G) under the UEFI environment.

This project attempts to start from a tiny, hand-assembled binary "Seed" and
iteratively compiling higher-level languages until (hopefully) a full toolchain
is realized.

## The Plan

The goal is to reach a self-hosting system through a series of "stages" or
"bootstrap levels":

1.  **Stage 0 (The Seed):** A minimal hex-to-binary compiler written in raw
    machine code (hex strings). It supports comments and ignores whitespace.
2.  **Stage 1 (Hex+):** Use the Seed to build a slightly better assembler that
    supports labels and basic symbol resolution.
3.  **Stage 2 (Intermediate):** Build a small, specialized systems language
    (likely a Forth or a simplified C-subset).
4.  **Stage 3 (Full Circle):** Implement the final high-level language and
    compiler that can compile itself.

## Current Status

- [x] **Nix Toolchain:** Reproducible environment with QEMU and UEFI firmware.
- [x] **Doc Generator:** Automated tool for UEFI struct ABI calculations.
- [ ] **Seed Logic:** Hex-to-binary logic implemented in `seed.hx0`.
- [ ] **Stage 1 Transition:** Currently writing the first "proper" assembler
      logic in hex.

## Getting Started

If you are new to the project or want to understand the very first steps of the
bootstrap, **read [docs/seed.md](docs/seed.md) first.** It explains the `hx0`
specification and how the initial binary is constructed.

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
- `docs/uefi/`: Auto-generated Markdown documentation.
- `scripts/`: Internal toolchain scripts.
- `bootdir/`: The virtual disk content for the emulator.
