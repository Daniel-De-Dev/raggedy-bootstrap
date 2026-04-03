# The Seed

## Overview

The `seed.efi` is the first step in the bootstrapping chain. It is a minimal
compiler hand-assembled into a UEFI-compatible RISC-V 64-bit binary. Its primary
purpose is to provide an escape from raw hex editing by allowing the developer
to write subsequent code in the [`hx0` format](specs/hx0.md).

## Environment & Architecture

- **Architecture:** RISC-V 64-bit
- **Target:** UEFI Bare Metal
- **Execution:** Runs as a standard UEFI Application
  (`EFI_IMAGE_SUBSYSTEM_EFI_APPLICATION`).

## The Bootstrapping Process

To begin, the initial Seed must be manually planted:

1. **Beginning:** Manually enter the hex found in `seed.hx0` into a binary file
   using a hex editor (or use the "pre-compiled" version, verifying the byte
   contents match).
1. **Setup:** Place `seed.efi` in the root to be executed trough UEFI shell or
   copy it to `bootdir/EFI/BOOT/BOOTRISCV64.EFI`. Then place your target
   [`hx0` format](specs/hx0.md) file in `bootdir/` or whatever is the
   FAT-formatted drive and name it `src.hx0` (this filename is hardcoded).
1. **Execution:** Boot the RISC-V based UEFI system. The Seed will execute,
   locate `src.hx0`, parse it according to the language spec, and generate
   `out.efi`.
1. **Verification:** To test self-hosting, compile the `seed.hx0` implementation
   itself. Compare the resulting `out.efi` against the hand-assembled
   `BOOTRISCV64.EFI` by manual inspection (or using a checksum or diff tool). If
   they are byte-for-byte identical, the system has successfully self-hosted.
