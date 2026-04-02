{ ... }:
{
  perSystem =
    { pkgs, ... }:
    let
      pythonEnv = pkgs.python3.withPackages (ps: [ ps.pyyaml ]);
    in
    {
      checks = {
        docs-sync = pkgs.stdenv.mkDerivation {
          name = "docs-sync-check";
          src = pkgs.lib.cleanSource ../.;

          buildInputs = [ pythonEnv ];

          buildPhase = ''
            python3 scripts/gen_docs.py --check
          '';

          installPhase = "touch $out";
        };
      };
    };
}
