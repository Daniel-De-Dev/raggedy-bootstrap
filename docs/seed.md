# The Seed

## Overview

The `seed.efi` is the first step in the bootstrapping chain. It is a minimal compiler hand-assembled into a UEFI-compatible RISC-V 64-bit binary. Its primary purpose is to provide an escape from raw hex editing by allowing the developer to write subsequent code in the structured [`hx0` format](specs/hx0.md).

## Environment & Architecture

* **Architecture:** RISC-V 64-bit (RV64G)
* **Target:** UEFI Bare Metal (PE/COFF executable)
* **Execution:** Runs as a standard UEFI Application (`EFI_IMAGE_SUBSYSTEM_EFI_APPLICATION`).

## The Bootstrapping Process

To begin, the initial Seed must be manually planted:

1. **Beginning:** Manually enter the hex found in `seed.hx0` into a binary file using a hex editor (or use the "pre-compiled" version, verifying the byte contents match). 
1. **Naming Convention:** While it is conceptually `seed.efi`, UEFI firmware strictly requires the default bootloader to be named `BOOTRISCV64.EFI`. Save the file to `/EFI/BOOT/BOOTRISCV64.EFI` on the FAT drive.
1. **Setup:** Place your target [`hx0` format](specs/hx0.md) file in the root of the FAT-formatted virtual drive and name it `src.hx0` (this filename is hardcoded).
1. **Execution:** Boot the RISC-V based UEFI system. The Seed will execute, locate `src.hx0`, parse it according to the language spec, and generate `out.efi`.
1. **Verification:** To test self-hosting, compile the `seed.hx0` implementation itself. Compare the resulting `out.efi` against the hand-assembled `BOOTRISCV64.EFI` by manual inspection (or using a checksum or diff tool). If they are byte-for-byte identical, the system has successfully self-hosted.
