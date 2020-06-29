#!/usr/bin/env python3

from utils import get_input

def solution():
    data = get_input(1)
    chars = {'(': 1, ')': -1}
    basement = 1
    for position, char in enumerate(data):
        basement += chars[char]
        if basement < 0:
            return position
