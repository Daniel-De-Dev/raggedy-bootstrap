---
uefi_version: 2.11
architecture: 64
---

<!-- THIS FILE IS AUTO-GENERATED FROM YAML DATA. DO NOT EDIT DIRECTLY! -->

# [EFI_FILE_READ](https://uefi.org/specs/UEFI/2.11/13_Protocols_Media_Access.html#efi-file-protocol-read)

**Function Pointer**

- **Size**: `8` bytes
- **Returns**: `EFI_STATUS`

### Parameters

| Type | Name |
| :--- | :--- |
| [`EFI_FILE_PROTOCOL*`](EFI_FILE_PROTOCOL.md) | `This` |
| [`UINTN*`](UINTN.md) | `BufferSize` |
| `VOID*` | `Buffer` |
