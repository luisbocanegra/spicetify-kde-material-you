# spicetify-kde-material-you

Quick dirty spicetify theme for [kde-material-you-colors](https://github.com/luisbocanegra/kde-material-you-colors)

## config-xpui.ini

```ini
[Setting]
current_theme           = MaterialYou
replace_colors          = 1
color_scheme            = materialyou
inject_css              = 1
overwrite_assets        = 1
inject_theme_js         = 1
```

optional tinted scrollable artist page img

```ini
[AdditionalOptions]
extensions            = scrollArtistImg.js
```

## hook (on_change_hook=/path/to/kde-material-you-hooks.sh)

```sh
#!/bin/bash

python /path/to/material-you-spicetify.py
```
