{
  description = "UEFI Bare Metal Bootstrap Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { nixpkgs, ... }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {
      buildInputs = with pkgs; [
        qemu
        OVMF
      ];

      shellHook = ''
        export OVMF_DIR="${pkgs.OVMF.fd}/FV"
        echo "UEFI Bootstrap Toolchain loaded."
      '';
    };
  };
}
