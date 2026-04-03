# Documentation

Welcome. This directory contains the documentation related to the project.

## 1. The Seed Compiler

The beginning of the bootstrap chain is `seed.hx0`, a basic "compiler" that
implements its own spec

Read further:

- [**The Seed Overview**](seed.md)
- [**hx0 Specification**](specs/hx0.md)

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
