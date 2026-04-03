---
uefi_version: 2.11
architecture: 64
---

<!-- THIS FILE IS AUTO-GENERATED FROM YAML DATA. DO NOT EDIT DIRECTLY! -->

# [EFI_FILE_OPEN](https://uefi.org/specs/UEFI/2.11/13_Protocols_Media_Access.html#efi-file-protocol-open)

**Function Pointer**

- **Size**: `8` bytes
- **Returns**: `EFI_STATUS`

### Parameters

| Type | Name |
| :--- | :--- |
| [`EFI_FILE_PROTOCOL*`](EFI_FILE_PROTOCOL.md) | `This` |
| [`EFI_FILE_PROTOCOL**`](EFI_FILE_PROTOCOL.md) | `NewHandle` |
| `CHAR16*` | `FileName` |
| [`UINT64`](UINT64.md) | `OpenMode` |
| [`UINT64`](UINT64.md) | `Attributes` |
