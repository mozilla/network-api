#!/usr/bin/env bash

mkdir -p media/images/shared

cp networkapi/static/shared/images/default.png media/images/shared

# Uninstall the fancy-shmancy media browser that doesn't work well with cloud based storage.
# pip uninstall filebrowser_safe --yes
