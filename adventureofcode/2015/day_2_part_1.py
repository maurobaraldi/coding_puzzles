#!/usr/bin/env python3

from utils import get_input


def solution():
    data = get_input(2).split()
    total = 0
    for box in data:
        l, w, h = map(int, box.split('x'))
        sheets = (2*l*w) + (2*w*h) + (2*h*l)
        extra = min([l*w, w*h, h*l])
        total = total + sheets + extra
    return total

