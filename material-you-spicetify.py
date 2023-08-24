#!/usr/bin/python3
from pathlib import Path
import json
import configparser
import os
import time

MATERIAL_YOU_JSON_FILE = "/tmp/kde-material-you-colors.json"
SPICETIFY_COLORS_FILE = "/home/luis/.config/spicetify/Themes/Lightly/color.ini"
MATERIAL_YOU_CONFIG = "/home/luis/.config/kde-material-you-colors/config.conf"
HOME = str(Path.home())
KDE_GLOBALS = HOME + "/.config/kdeglobals"


def kde_globals_light():
    kdeglobals = configparser.ConfigParser()
    if os.path.exists(KDE_GLOBALS):
        try:
            kdeglobals.read(KDE_GLOBALS)
            if "General" in kdeglobals:
                general = kdeglobals["General"]
                if "ColorScheme" in general:
                    if "MaterialYouDark" in general["ColorScheme"]:
                        return False
                    elif "MaterialYouLight" in general["ColorScheme"]:
                        return True
            else:
                return None
        except Exception as e:
            print(f"Error:\n{e}")
            return None
    else:
        return None


# print(kde_globals_light())


def get_light():
    if os.path.exists(MATERIAL_YOU_CONFIG):
        # print(F"{MATERIAL_YOU_CONFIG} EXISTS")
        material_you_config = configparser.ConfigParser()
        try:
            material_you_config.read(MATERIAL_YOU_CONFIG)
            if "CUSTOM" in material_you_config:
                custom = material_you_config["CUSTOM"]
                if custom.getboolean("light") is not None:
                    return custom.getboolean("light")
                else:
                    return kde_globals_light()

        except Exception:
            return kde_globals_light()

    else:
        return None


# print(get_light())
colors_old = None


def export_theme(colors_conf, light_mode):
    # print("AAAA")
    if light_mode is True:
        # print("applying light theme...")
        colors_conf["materialyou"]["text"] = colors["palettes"]["primary"]["20"]
        colors_conf["materialyou"]["subtext"] = colors["palettes"]["secondary"]["30"]
        colors_conf["materialyou"]["scrollbar"] = colors["schemes"]["light"]["outline"]
        colors_conf["materialyou"]["divider"] = colors["palettes"]["secondary"]["70"]
        colors_conf["materialyou"]["white"] = colors["schemes"]["light"]["outline"]
        colors_conf["materialyou"]["main"] = colors["extras"]["light"]["surface"]
        colors_conf["materialyou"]["sidebar"] = colors["extras"]["light"]["surface"]
        colors_conf["materialyou"]["player"] = colors["extras"]["light"]["surface3"]
        colors_conf["materialyou"]["card"] = colors["extras"]["light"]["surface3"]
        colors_conf["materialyou"]["shadow"] = colors["schemes"]["light"]["shadow"]
        colors_conf["materialyou"]["button"] = colors["schemes"]["light"]["primary"]
        colors_conf["materialyou"]["button-active"] = colors["schemes"]["light"][
            "outline"
        ]
        colors_conf["materialyou"]["button-disabled"] = colors["schemes"]["light"][
            "outline"
        ]
        colors_conf["materialyou"]["tab-active"] = colors["schemes"]["light"]["outline"]
        colors_conf["materialyou"]["notification"] = "50bf58"
        colors_conf["materialyou"]["notification-error"] = colors["schemes"]["light"][
            "outline"
        ]
    elif light_mode is False:
        # print("applying dark theme...")
        colors_conf["materialyou"]["text"] = colors["palettes"]["primary"]["92"]
        colors_conf["materialyou"]["subtext"] = colors["palettes"]["secondary"]["80"]
        colors_conf["materialyou"]["scrollbar"] = colors["schemes"]["dark"]["outline"]
        colors_conf["materialyou"]["divider"] = colors["schemes"]["dark"][
            "inverseOnSurface"
        ]
        colors_conf["materialyou"]["white"] = colors["schemes"]["dark"]["outline"]
        colors_conf["materialyou"]["main"] = colors["extras"]["dark"]["surface"]
        colors_conf["materialyou"]["sidebar"] = colors["extras"]["dark"]["surface"]
        colors_conf["materialyou"]["player"] = colors["extras"]["dark"]["surface3"]
        colors_conf["materialyou"]["card"] = colors["extras"]["dark"]["surface3"]
        colors_conf["materialyou"]["shadow"] = colors["schemes"]["dark"]["surface"]
        colors_conf["materialyou"]["button"] = colors["schemes"]["dark"]["primary"]
        colors_conf["materialyou"]["button-active"] = colors["schemes"]["dark"][
            "outline"
        ]
        colors_conf["materialyou"]["button-disabled"] = colors["schemes"]["dark"][
            "outline"
        ]
        colors_conf["materialyou"]["tab-active"] = colors["schemes"]["dark"]["outline"]
        colors_conf["materialyou"]["notification"] = "6bff75"
        colors_conf["materialyou"]["notification-error"] = colors["schemes"]["dark"][
            "outline"
        ]

    # print("AAAA")
    # print(colors_conf['materialyou']['text'])
    with open(SPICETIFY_COLORS_FILE, "w") as configfile:
        colors_conf.write(configfile, space_around_delimiters=True)
        # print("done...")


# while True:

colors = None
try:
    with open(MATERIAL_YOU_JSON_FILE, "r") as colors:
        colors = json.loads(colors.read().replace("#", ""))
        # print(colors)
except Exception:
    # time.sleep(2)
    # continue
    pass

light_mode = get_light()
colors_new = colors
light_mode_old = None
changed = colors_new != colors_old or light_mode != light_mode_old
if colors is not None and changed and light_mode is not None:
    if os.path.exists(MATERIAL_YOU_JSON_FILE):
        colors_conf = configparser.ConfigParser()
        # preserve case
        colors_conf.optionxform("str")

        if os.path.exists(SPICETIFY_COLORS_FILE):
            # print("colors.ini exists")

            colors_conf.read(SPICETIFY_COLORS_FILE)
            if "materialyou" not in colors_conf:
                colors_conf.add_section("materialyou")
            export_theme(colors_conf, light_mode)

colors_old = colors_new
light_mode_old = light_mode
# exit(0)
# time.sleep(1)
