#!/usr/bin/env python3

from importlib import import_module
from glob import glob

solutions = sorted([f.replace('.py', '') for f in glob('day*.py')])

for s in solutions:
    problem = import_module('%s' % s)
    print("Solution for {} {} {} {}: {}".format(*s.split('_'), problem.solution()))
