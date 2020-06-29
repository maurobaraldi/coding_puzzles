#!/usr/bin/env python3

from utils import get_input

def solution():
    data = get_input(1)
    up = data.count('(')
    down = data.count(')')
    return up - down
