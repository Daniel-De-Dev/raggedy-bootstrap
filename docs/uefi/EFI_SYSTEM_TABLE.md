---
uefi_version: 2.11
architecture: 64
---

<!-- THIS FILE IS AUTO-GENERATED FROM YAML DATA. DO NOT EDIT DIRECTLY! -->

# [EFI_SYSTEM_TABLE](https://uefi.org/specs/UEFI/2.11/04_EFI_System_Table.html#efi-system-table-1)

**Note:** in RISC-V Passed as `a1` directly by the firmware at the entry point of the bare-metal executable.

| Offset (Dec) | Offset (Hex) | Type | Name | Size | Padding |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `0x00` | [`EFI_TABLE_HEADER`](EFI_TABLE_HEADER.md) | `Hdr` | 24 | 0 |
| 24 | `0x18` | `CHAR16*` | `FirmwareVendor` | 8 | 0 |
| 32 | `0x20` | [`UINT32`](UINT32.md) | `FirmwareRevision` | 4 | 0 |
| 36 | `0x24` | [`EFI_HANDLE`](EFI_HANDLE.md) | `ConsoleInHandle` | 8 | 4 |
| 48 | `0x30` | `EFI_SIMPLE_TEXT_INPUT_PROTOCOL*` | `ConIn` | 8 | 0 |
| 56 | `0x38` | [`EFI_HANDLE`](EFI_HANDLE.md) | `ConsoleOutHandle` | 8 | 0 |
| 64 | `0x40` | `EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL*` | `ConOut` | 8 | 0 |
| 72 | `0x48` | [`EFI_HANDLE`](EFI_HANDLE.md) | `StandardErrorHandle` | 8 | 0 |
| 80 | `0x50` | `EFI_SIMPLE_TEXT_OUTPUT_PROTOCOL*` | `StdErr` | 8 | 0 |
| 88 | `0x58` | `EFI_RUNTIME_SERVICES*` | `RuntimeServices` | 8 | 0 |
| 96 | `0x60` | `EFI_BOOT_SERVICES*` | `BootServices` | 8 | 0 |
| 104 | `0x68` | [`UINTN`](UINTN.md) | `NumberOfTableEntries` | 8 | 0 |
| 112 | `0x70` | `EFI_CONFIGURATION_TABLE*` | `ConfigurationTable` | 8 | 0 |
