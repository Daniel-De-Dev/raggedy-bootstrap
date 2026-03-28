{
  description = "RISC-V UEFI Bare Metal Bootstrap Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
    treefmt-nix = {
      url = "github:numtide/treefmt-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, treefmt-nix, ... }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};

      treefmtEval = treefmt-nix.lib.evalModule pkgs {
        projectRootFile = "flake.nix";

        settings.global.excludes = [ "docs/uefi/*.md" ];

        programs = {
          nixfmt.enable = true;
          black.enable = true;
          prettier = {
            enable = true;
            includes = [ "*.md" "*.yaml" "*.yml" ];
            settings = {
              printWidth = 80;
              proseWrap = "always";
            };
          };
        };
      };
    in {
      formatter.${system} = treefmtEval.config.build.wrapper;

      checks.${system}.formatting = treefmtEval.config.build.check self;

      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          qemu
          pkgsCross.riscv64.OVMF.fd
          python3
          python3Packages.pyyaml

          (writeShellScriptBin "boot-riscv" ''
            cp -f ${pkgsCross.riscv64.OVMF.fd}/FV/RISCV_VIRT_VARS.fd ./_vars.fd
            chmod +w ./_vars.fd

            qemu-system-riscv64 \
              -M virt \
              -m 256M \
              -drive if=pflash,format=raw,unit=0,file=${pkgsCross.riscv64.OVMF.fd}/FV/RISCV_VIRT_CODE.fd,readonly=on \
              -drive if=pflash,format=raw,unit=1,file=./_vars.fd \
              -drive file=fat:rw:bootdir,format=raw,if=virtio \
              -device virtio-gpu-pci \
              -device qemu-xhci \
              -device usb-kbd
          '')
        ];

        shellHook = ''
          echo " RISC-V UEFI Bootstrap Toolchain loaded "
          mkdir -p bootdir/EFI/BOOT
          if [ ! -f bootdir/EFI/BOOT/BOOTRISCV64.EFI ]; then
            echo "Warning: No BOOTRISCV64.EFI found in bootdir"
          fi
        '';
      };
    };
}
