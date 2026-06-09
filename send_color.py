#!/usr/bin/python3

import hid
import sys

# USB IDs
VID = 0x3297
PID = 0x1969

# CONTROL BYTES
SEND_COLOR = 0x00
TOGGLE_COLOR_MODE = 0x01


def send_stuff(data):
    for d in hid.enumerate(VID, PID):
        # there are multiple parts of the keyboard that accept hid, we should choose the one that listens to our raw hid
        if d['usage_page'] in (0xff60, 0xff00):
            with hid.Device(path=d['path']) as dev:
                dev.nonblocking = 1
                # the first bit should not be necessary like that, but we only read from the second bit on so...
                dev.write(bytes([0xff] + data + ([0x00] * (31 - len(data)))))

            
def send_rgb(r, g, b):
    data = [SEND_COLOR, r, g, b]
    send_stuff(data)
    

def individual_color_from_hex(h):
    return int(h, 16)


def convert_from_hex(h):
    return [individual_color_from_hex(h[1+2 * i:3+2*i]) for i in range(3)]


def main():
    if sys.argv[1][0] == "#":
        r, g, b = convert_from_hex(sys.argv[1])
        send_rgb(r, g, b)
    elif sys.argv[1] == "toggle_mode":
        send_stuff([TOGGLE_COLOR_MODE])
    else:
        print("unknown mode")

if __name__ == "__main__":
    main()
