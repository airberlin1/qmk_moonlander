#!/usr/bin/python3

import hid
import sys

# USB IDs
VID = 0x3297
PID = 0x1969

def send_rgb(r, g, b):
    with hid.Device(VID, PID) as dev:
        dev.nonblocking = 1
        data = [r, g, b]
        dev.write(bytes([0x00] + data))
        print(data)


def individual_color_from_hex(h):
    return int(h, 16)


def convert_from_hex(h):
    return [individual_color_from_hex(h[1+2 * i:3+2*i]) for i in range(3)]


def main():
    if sys.argv[1][0] == "#":
       r, g, b = convert_from_hex(sys.argv[1])
       send_rgb(r, g, b)


if __name__ == "__main__":
    main()
