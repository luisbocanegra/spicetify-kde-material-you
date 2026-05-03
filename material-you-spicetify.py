#!/usr/bin/python3
import getpass
from pathlib import Path
import json
import configparser
import os
import re

USER = getpass.getuser()
HOME = str(Path.home())
MATERIAL_YOU_JSON_FILE = f"/tmp/kde-material-you-colors-{USER}.json"
SPICETIFY_COLORS_FILE = HOME + "/.config/spicetify/Themes/MaterialYou/color.ini"


def to_kebab_case(text: str) -> str:
    kebab = re.sub(r"(?<!^)(?=[A-Z])", "-", text).lower()
    return kebab


def export_scheme_colors(section: configparser.SectionProxy, palette: dict, prefix=""):
    for role, color in palette.items():
        section[f"{prefix}{to_kebab_case(role)}"] = color


def export_custom_colors(
    section: configparser.SectionProxy, colors: dict, scheme_name: str
):
    for custom_role, custom_colors in colors.get("custom", {}).items():

        prefix = f"custom-{to_kebab_case(custom_role)}-"
        export_scheme_colors(section, custom_colors.get(scheme_name, {}), prefix)


def copy_section(source: configparser.SectionProxy, target: configparser.SectionProxy):
    target.clear()
    for role, color in source.items():
        target[role] = color


def export_theme(cfg: configparser.ConfigParser, colors: dict):
    if not "light" in cfg:
        cfg.add_section("light")
    if not "dark" in cfg:
        cfg.add_section("dark")
    if not "auto" in cfg:
        cfg.add_section("auto")

    light_mode = colors["light"]

    export_scheme_colors(section=cfg["light"], palette=colors["schemes"]["light"])
    export_custom_colors(section=cfg["light"], colors=colors, scheme_name="light")

    export_scheme_colors(section=cfg["dark"], palette=colors["schemes"]["dark"])
    export_custom_colors(section=cfg["dark"], colors=colors, scheme_name="dark")

    auto_scheme = "light" if light_mode else "dark"
    for role, color in cfg[auto_scheme].items():
        cfg["auto"][role] = color

    with open(SPICETIFY_COLORS_FILE, "w", encoding="utf-8") as config_file:
        cfg.write(config_file, space_around_delimiters=True)


def main():
    colors = None
    try:
        with open(MATERIAL_YOU_JSON_FILE, "r", encoding="utf-8") as colors_file:
            colors = json.loads(colors_file.read().replace("#", ""))
    except (OSError, json.JSONDecodeError):
        pass

    if colors is not None:
        if os.path.exists(MATERIAL_YOU_JSON_FILE):
            colors_conf = configparser.ConfigParser()
            colors_conf.optionxform = str

            if os.path.exists(SPICETIFY_COLORS_FILE):
                colors_conf.read(SPICETIFY_COLORS_FILE)
                export_theme(colors_conf, colors)


if __name__ == "__main__":
    main()
