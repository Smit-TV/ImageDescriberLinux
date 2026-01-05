#!/usr/bin/env bash

echo "Installing..."
mkdir ~/.local/share/ImageDescriber/ -p
cp ./*.py ~/.local/share/ImageDescriber/
echo "Done"
echo "Files copied to ~/.local/share/ImageDescriber/"