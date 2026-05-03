#!/usr/bin/env bash

FILES=("./MaterialYou/user.css")

inotifywait -m -e modify "${FILES[@]}" |
while read -r file_path file_event file_name; do
    cp ./MaterialYou/user.css "$HOME/.config/spicetify/Themes/MaterialYou/user.css"
done
