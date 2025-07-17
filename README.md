# QMK Moonlander
My current QMK firmware for a ZSA Moonlander keyboard, used to change color of some keys with theme change on PC.
This build has been adapted from my Colemak-like layout, initially changed from TheOneWhoCodes' layout [Rainbow Cake v2 (Colemak Mod DH)](https://configure.zsa.io/moonlander/layouts/Ze0bo/latest/0), utilising home row modifiers. 

If I remember, here you can find my current layout (with as much functionality as I could add there) on oryx:

# Build
Instructions are for compiling against [ZSA's QMK fork](https://github.com/zsa/qmk_firmware/). I have not tested compiling against mainline QMK.

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
qmk setup zsa/qmk_firmware -b firmware25
qmk compile -kb zsa/moonlander -km default
```
This sets up qmk with the ZSA fork and tries to compile the default layout for the moonlander. If successful, it should say the some positive things like "The firmware size is fine" and no negative things. You might want to specify a different branch for the firmware, change firmware24 to the wanted branch name for that.

I had to add 

``` c
enum planck_ez_keycodes {
    TOGGLE_LAYER_COLOR = QK_KB_0,
    LED_LEVEL,
};
```
manually to moonlander.h, but I hope that is not the case anymore when reading this.

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

