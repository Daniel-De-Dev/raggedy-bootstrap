{ ... }:
{
  perSystem =
    { pkgs, ... }:
    {
      treefmt.config = {
        projectRootFile = "flake.nix";

        settings.global.excludes = [
          ".envrc"
          "*.hx0"
          "docs/uefi/*.md"
        ];

        programs = {
          nixfmt = {
            enable = true;
            package = pkgs.nixfmt-rfc-style;
          };
          black.enable = true;
          prettier = {
            enable = true;
            includes = [
              "*.md"
              "*.yaml"
              "*.yml"
            ];
            settings = {
              printWidth = 80;
              proseWrap = "always";
            };
          };
        };
      };
    };
}
