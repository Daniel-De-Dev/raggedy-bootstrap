# Documentation

Welcome. This directory contains the documentation related to the project.

## 1. The Seed Compiler

The absolute beginning of the bootstrap chain is `seed.hx0`, a minimalist
compiler written directly in raw machine code hex.

- [**The Seed Overview**](seed.md): Explains the runtime environment, the
  compilation process, and how self-hosting verification works.

- [**hx0 Specification**](specs/hx0.md): The specification for the stage-0
  language.

## 2. UEFI ABI Reference

Since the seed is written directly in machine code, there is no C compiler to
automatically calculate structure offsets, padding, or function pointer sizes
for the UEFI environment.

Couldn't find anything else to easily get these values with good navigation, so
a doc generator was created. The [**`uefi/`**](uefi/) directory contains a
markdown map of the UEFI ABI. (**not comprehensive**)

- It is auto-generated from the YAML definitions found in
  [`structs/uefi/`](structs/uefi/).

- **Starting Point:** Begin exploring at the
  [**`EFI_SYSTEM_TABLE`**](uefi/EFI_SYSTEM_TABLE.md), which is the root
  structure passed directly to our bare-metal executable by the firmware.
