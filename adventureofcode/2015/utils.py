#!/usr/bin/env python3


def get_input(day: int) -> str:
    with open('./inputs/day_{}'.format(day)) as data:
        return data.read()
