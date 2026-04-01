---
uefi_version: 2.11
architecture: 64
---

<!-- THIS FILE IS AUTO-GENERATED FROM YAML DATA. DO NOT EDIT DIRECTLY! -->

# [EFI_LOCATE_PROTOCOL](https://uefi.org/specs/UEFI/2.11/07_Services_Boot_Services.html#efi-boot-services-locateprotocol)

**Note:** The returned `Interface` depends on the `Protocol` GUID provided.

**Function Pointer**

- **Size**: `8` bytes
- **Returns**: `EFI_STATUS`

### Parameters

| Type | Name |
| :--- | :--- |
| [`EFI_GUID*`](EFI_GUID.md) | `Protocol` |
| `VOID*` | `Registration` |
| `VOID**` | `Interface` |
