#!/bin/bash

if [ -z "$1" ]; then
    echo "File path not provided"
    exit 1
fi

file_path="$1"

for file in "$file_path"/*; do
    if [ -f "$file" ]; then
        if [ "${file##*.}" != "mp4" ]; then
            new_file="${file}.mp4"
            mv "$file" "$new_file"
        fi
    fi
done