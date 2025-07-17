# QMK Moonlander
My current QMK firmware for a ZSA Moonlander keyboard, used to change color of some keys with theme change on PC.
This build has been adapted from my Colemak-like layout, initially changed from TheOneWhoCodes' layout [Rainbow Cake v2 (Colemak Mod DH)](https://configure.zsa.io/moonlander/layouts/Ze0bo/latest/0), utilising home row modifiers. 

# Build
Instructions are for compiling against mainline QMK. Compiling against the ZSA fork should work, but I have not tested it.

## Environment Setup
Follow the [QMK Setup guide](https://docs.qmk.fm/newbs_getting_started#set-up-your-environment). Specific instructions are given for Arch and Void:
### Needed binaries
Arch:

``` sh
pacman --needed --noconfirm -S git python-pip libffi
pacman -S qmk
```

Void:

``` sh
xbps-install -y git python3-pip
python3 -m pip install --user qmk
```
### Setup and Testing
For both Arch and Void, run

``` sh
qmk setup qmb/qmk_firmware
qmk compile -kb zsa/moonlander -km default
```

Also, some file permissions might need to updated. Run

``` sh
chmod +x build.sh
chmod +x send_color.py
```
to achieve that.

## Compile
Run

``` sh
./build.sh
```
in the project directory.

## Flash
Run 

``` sh
qmk flash -kb zsa/moonlander -km colors
```

# Usage

Run

``` sh
./send_color "#ff00ff"
```
with whatever color you like. The default format is "#rrggbb" in base 16.

# Further Ideas
This should be reasonably expandable to allow for complete colormaps (or just a set of colors) to be sent by using an additional control bit in the raw hid. I am currently happy with a single color being changed, but I might come back to this in the future.

Also, colors are lost on boot. While it is also easier to implement that way, I like that functionality, so I don't plan on changing that. When rebooting, default colors are used until a color is sent.
