---
uefi_version: 2.11
architecture: 64
---

<!-- THIS FILE IS AUTO-GENERATED FROM YAML DATA. DO NOT EDIT DIRECTLY! -->

# [EFI_BOOT_SERVICES](https://uefi.org/specs/UEFI/2.11/04_EFI_System_Table.html#efi-boot-services-table)

| Offset (Dec) | Offset (Hex) | Type | Name | Size | Padding |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | `0x00` | [`EFI_TABLE_HEADER`](EFI_TABLE_HEADER.md) | `Hdr` | 24 | 0 |
| 24 | `0x18` | [`EFI_RAISE_TPL`](EFI_RAISE_TPL.md) | `RaiseTPL` | 8 | 0 |
| 32 | `0x20` | [`EFI_RESTORE_TPL`](EFI_RESTORE_TPL.md) | `RestoreTPL` | 8 | 0 |
| 40 | `0x28` | [`EFI_ALLOCATE_PAGES`](EFI_ALLOCATE_PAGES.md) | `AllocatePages` | 8 | 0 |
| 48 | `0x30` | [`EFI_FREE_PAGES`](EFI_FREE_PAGES.md) | `FreePages` | 8 | 0 |
| 56 | `0x38` | [`EFI_GET_MEMORY_MAP`](EFI_GET_MEMORY_MAP.md) | `GetMemoryMap` | 8 | 0 |
| 64 | `0x40` | [`EFI_ALLOCATE_POOL`](EFI_ALLOCATE_POOL.md) | `AllocatePool` | 8 | 0 |
| 72 | `0x48` | [`EFI_FREE_POOL`](EFI_FREE_POOL.md) | `FreePool` | 8 | 0 |
| 80 | `0x50` | [`EFI_CREATE_EVENT`](EFI_CREATE_EVENT.md) | `CreateEvent` | 8 | 0 |
| 88 | `0x58` | [`EFI_SET_TIMER`](EFI_SET_TIMER.md) | `SetTimer` | 8 | 0 |
| 96 | `0x60` | [`EFI_WAIT_FOR_EVENT`](EFI_WAIT_FOR_EVENT.md) | `WaitForEvent` | 8 | 0 |
| 104 | `0x68` | [`EFI_SIGNAL_EVENT`](EFI_SIGNAL_EVENT.md) | `SignalEvent` | 8 | 0 |
| 112 | `0x70` | [`EFI_CLOSE_EVENT`](EFI_CLOSE_EVENT.md) | `CloseEvent` | 8 | 0 |
| 120 | `0x78` | [`EFI_CHECK_EVENT`](EFI_CHECK_EVENT.md) | `CheckEvent` | 8 | 0 |
| 128 | `0x80` | [`EFI_INSTALL_PROTOCOL_INTERFACE`](EFI_INSTALL_PROTOCOL_INTERFACE.md) | `InstallProtocolInterface` | 8 | 0 |
| 136 | `0x88` | [`EFI_REINSTALL_PROTOCOL_INTERFACE`](EFI_REINSTALL_PROTOCOL_INTERFACE.md) | `ReinstallProtocolInterface` | 8 | 0 |
| 144 | `0x90` | [`EFI_UNINSTALL_PROTOCOL_INTERFACE`](EFI_UNINSTALL_PROTOCOL_INTERFACE.md) | `UninstallProtocolInterface` | 8 | 0 |
| 152 | `0x98` | [`EFI_HANDLE_PROTOCOL`](EFI_HANDLE_PROTOCOL.md) | `HandleProtocol` | 8 | 0 |
| 160 | `0xA0` | `VOID*` | `Reserved` | 8 | 0 |
| 168 | `0xA8` | [`EFI_REGISTER_PROTOCOL_NOTIFY`](EFI_REGISTER_PROTOCOL_NOTIFY.md) | `RegisterProtocolNotify` | 8 | 0 |
| 176 | `0xB0` | [`EFI_LOCATE_HANDLE`](EFI_LOCATE_HANDLE.md) | `LocateHandle` | 8 | 0 |
| 184 | `0xB8` | [`EFI_LOCATE_DEVICE_PATH`](EFI_LOCATE_DEVICE_PATH.md) | `LocateDevicePath` | 8 | 0 |
| 192 | `0xC0` | [`EFI_INSTALL_CONFIGURATION_TABLE`](EFI_INSTALL_CONFIGURATION_TABLE.md) | `InstallConfigurationTable` | 8 | 0 |
| 200 | `0xC8` | [`EFI_IMAGE_LOAD`](EFI_IMAGE_LOAD.md) | `LoadImage` | 8 | 0 |
| 208 | `0xD0` | [`EFI_IMAGE_START`](EFI_IMAGE_START.md) | `StartImage` | 8 | 0 |
| 216 | `0xD8` | [`EFI_EXIT`](EFI_EXIT.md) | `Exit` | 8 | 0 |
| 224 | `0xE0` | [`EFI_IMAGE_UNLOAD`](EFI_IMAGE_UNLOAD.md) | `UnloadImage` | 8 | 0 |
| 232 | `0xE8` | [`EFI_EXIT_BOOT_SERVICES`](EFI_EXIT_BOOT_SERVICES.md) | `ExitBootServices` | 8 | 0 |
| 240 | `0xF0` | [`EFI_GET_NEXT_MONOTONIC_COUNT`](EFI_GET_NEXT_MONOTONIC_COUNT.md) | `GetNextMonotonicCount` | 8 | 0 |
| 248 | `0xF8` | [`EFI_STALL`](EFI_STALL.md) | `Stall` | 8 | 0 |
| 256 | `0x100` | [`EFI_SET_WATCHDOG_TIMER`](EFI_SET_WATCHDOG_TIMER.md) | `SetWatchdogTimer` | 8 | 0 |
| 264 | `0x108` | [`EFI_CONNECT_CONTROLLER`](EFI_CONNECT_CONTROLLER.md) | `ConnectController` | 8 | 0 |
| 272 | `0x110` | [`EFI_DISCONNECT_CONTROLLER`](EFI_DISCONNECT_CONTROLLER.md) | `DisconnectController` | 8 | 0 |
| 280 | `0x118` | [`EFI_OPEN_PROTOCOL`](EFI_OPEN_PROTOCOL.md) | `OpenProtocol` | 8 | 0 |
| 288 | `0x120` | [`EFI_CLOSE_PROTOCOL`](EFI_CLOSE_PROTOCOL.md) | `CloseProtocol` | 8 | 0 |
| 296 | `0x128` | [`EFI_OPEN_PROTOCOL_INFORMATION`](EFI_OPEN_PROTOCOL_INFORMATION.md) | `OpenProtocolInformation` | 8 | 0 |
| 304 | `0x130` | [`EFI_PROTOCOLS_PER_HANDLE`](EFI_PROTOCOLS_PER_HANDLE.md) | `ProtocolsPerHandle` | 8 | 0 |
| 312 | `0x138` | [`EFI_LOCATE_HANDLE_BUFFER`](EFI_LOCATE_HANDLE_BUFFER.md) | `LocateHandleBuffer` | 8 | 0 |
| 320 | `0x140` | [`EFI_LOCATE_PROTOCOL`](EFI_LOCATE_PROTOCOL.md) | `LocateProtocol` | 8 | 0 |
| 328 | `0x148` | [`EFI_INSTALL_MULTIPLE_PROTOCOL_INTERFACES`](EFI_INSTALL_MULTIPLE_PROTOCOL_INTERFACES.md) | `InstallMultipleProtocolInterfaces` | 8 | 0 |
| 336 | `0x150` | [`EFI_UNINSTALL_MULTIPLE_PROTOCOL_INTERFACES`](EFI_UNINSTALL_MULTIPLE_PROTOCOL_INTERFACES.md) | `UninstallMultipleProtocolInterfaces` | 8 | 0 |
| 344 | `0x158` | [`EFI_CALCULATE_CRC32`](EFI_CALCULATE_CRC32.md) | `CalculateCrc32` | 8 | 0 |
| 352 | `0x160` | [`EFI_COPY_MEM`](EFI_COPY_MEM.md) | `CopyMem` | 8 | 0 |
| 360 | `0x168` | [`EFI_SET_MEM`](EFI_SET_MEM.md) | `SetMem` | 8 | 0 |
| 368 | `0x170` | [`EFI_CREATE_EVENT_EX`](EFI_CREATE_EVENT_EX.md) | `CreateEventEx` | 8 | 0 |
