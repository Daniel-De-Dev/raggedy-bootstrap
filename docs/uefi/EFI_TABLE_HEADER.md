---
uefi_version: 2.11
architecture: 64
---

<!-- THIS FILE IS AUTO-GENERATED FROM YAML DATA. DO NOT EDIT DIRECTLY! -->

# [EFI_TABLE_HEADER](https://uefi.org/specs/UEFI/2.11/04_EFI_System_Table.html#efi-table-header)

| Offset (Dec) | Offset (Hex) | Type | Name | Size | Padding |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `0x00` | [`UINT64`](UINT64.md) | `Signature` | 8 | 0 |
| 8 | `0x08` | [`UINT32`](UINT32.md) | `Revision` | 4 | 0 |
| 12 | `0x0C` | [`UINT32`](UINT32.md) | `HeaderSize` | 4 | 0 |
| 16 | `0x10` | [`UINT32`](UINT32.md) | `CRC32` | 4 | 0 |
| 20 | `0x14` | [`UINT32`](UINT32.md) | `Reserved` | 4 | 0 |
