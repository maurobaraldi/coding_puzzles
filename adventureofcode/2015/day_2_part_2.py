#!/usr/bin/env python3

from utils import get_input


def solution():
    data = get_input(2).split()
    total = 0
    for box in data:
        l, w, h = map(int, box.split('x'))
        sides = sorted([l, w, h])
        total += sides[0] + sides[0] + sides[1] + sides[1] + (l * w * h)
    return total
