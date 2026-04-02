{ ... }:
{
  perSystem =
    { pkgs, ... }:
    let
      pythonEnv = pkgs.python3.withPackages (ps: [ ps.pyyaml ]);

      ovmfCode = "${pkgs.pkgsCross.riscv64.OVMF.fd}/FV/RISCV_VIRT_CODE.fd";
      ovmfVarsTemplate = "${pkgs.pkgsCross.riscv64.OVMF.fd}/FV/RISCV_VIRT_VARS.fd";

      qemuArgsBash = ''
        QEMU_ARGS=(
          -M virt
          -m 256M
          -drive "if=pflash,format=raw,unit=0,file=${ovmfCode},readonly=on"
          -drive "if=pflash,format=raw,unit=1,file=./_vars.fd"
          -drive "file=fat:rw:bootdir,format=raw,if=virtio"
          -device virtio-gpu-pci
          -device qemu-xhci
          -device usb-kbd
        )
      '';

      # Simple python implementation of hx0 compiler for debug purposes
      compileHx0 = pkgs.writeShellApplication {
        name = "compile-hx0";
        runtimeInputs = [
          pythonEnv
          pkgs.coreutils
        ];
        text = ''
          if [ -z "''${1:-}" ]; then
            echo "Usage: compile-hx0 <source.hx0>"
            exit 1
          fi

          mkdir -p bootdir/EFI/BOOT

          python3 -c '
          import sys, re
          hx = re.sub(r"#.*", "", sys.stdin.read())
          hx = re.sub(r"[^0-9A-Fa-f]", "", hx)
          sys.stdout.buffer.write(bytes.fromhex(hx))
          ' < "$1" > bootdir/EFI/BOOT/BOOTRISCV64.EFI

          echo "Compiled $1 to bootdir/EFI/BOOT/BOOTRISCV64.EFI"
        '';
      };

      bootRiscv = pkgs.writeShellApplication {
        name = "boot-riscv";
        runtimeInputs = [
          pkgs.qemu
          pkgs.coreutils
        ];
        text = ''
          if [ ! -f ./_vars.fd ]; then
            cp -f ${ovmfVarsTemplate} ./_vars.fd
            chmod +w ./_vars.fd
          fi

          mkdir -p bootdir/EFI/BOOT

          ${qemuArgsBash}
          qemu-system-riscv64 "''${QEMU_ARGS[@]}"
        '';
      };

      bootRiscvDebug = pkgs.writeShellApplication {
        name = "boot-riscv-debug";
        runtimeInputs = [
          pkgs.qemu
          pkgs.coreutils
        ];
        text = ''
          if [ ! -f ./_vars.fd ]; then
            cp -f ${ovmfVarsTemplate} ./_vars.fd
            chmod +w ./_vars.fd
          fi

          mkdir -p bootdir/EFI/BOOT
          echo "Starting QEMU in debug mode. Connect with 'gdb -q' in another terminal..."

          ${qemuArgsBash}
          qemu-system-riscv64 "''${QEMU_ARGS[@]}" -s -S
        '';
      };

    in
    {
      devShells.default = pkgs.mkShell {
        packages = [
          pkgs.qemu
          pkgs.pkgsCross.riscv64.OVMF.fd
          pkgs.gdb
          pythonEnv
          compileHx0
          bootRiscv
          bootRiscvDebug
        ];

        shellHook = ''
          echo " RISC-V UEFI Bootstrap Toolchain loaded "
          echo " Run 'compile-hx0 <file.hx0>' to quickly build an executable"
          echo " Run 'boot-riscv' to start the emulator "
          echo " Run 'boot-riscv-debug' to start paused with GDB server"
          echo " Run 'gdb -q' in a new terminal to connect to the debug server"
          mkdir -p bootdir/EFI/BOOT
          if [ ! -f bootdir/EFI/BOOT/BOOTRISCV64.EFI ]; then
            echo "Warning: No BOOTRISCV64.EFI found in bootdir/EFI/BOOT"
          fi
        '';
      };
    };
}
