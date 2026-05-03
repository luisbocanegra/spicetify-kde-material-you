# spicetify-kde-material-you

A spicetify theme for [kde-material-you-colors](https://github.com/luisbocanegra/kde-material-you-colors)

## Installation

```sh
git clone https://github.com/luisbocanegra/spicetify-kde-material-you
cd spicetify-kde-material-you
cp -r MaterialYou "$HOME/.config/spicetify/Themes/"
```

## Configuration

Enable the theme in `$HOME/.config/spicetify/config-xpui.ini`

```ini
[Setting]
current_theme           = MaterialYou
replace_colors          = 1
color_scheme            = auto
inject_css              = 1
```

`color_scheme` can be set to `light`, `dark` or `auto`. The `auto` option will switch between light and dark color schemes based on the `kde-material-you-colors` theme.

After changing the configuration, run `spicetify apply` to apply the changes.

## Update colors

**Manually:** run `material-you-spicetify.py` after `kde-material-you-colors`

**Automatically:** add the following to `$HOME/.config/kde-material-you-colors/config.conf`, replacing the path with the actual path to `material-you-spicetify.py`:

```ini
on_change_hook=/path/to/material-you-spicetify.py
```

If you are using the plasma widget, add `path/to/material-you-spicetify.py` to the *Run script* field in the widget settings.

## Reload colors without restarting Spotify

Run spicetify in watch mode

```sh
spicetify watch -s
```
