#! /usr/bin/env python3
# Author: SWilliams
# Description: This script will demo
"""
    Docstring:
"""

heroes = ['john', 'marie', 'diana', 'pele', 'ozzie']
for name in heroes:
    print(name, end="\n")

# iterate through list and modify the objects

idx = 0
for name in heroes:
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes = ", heroes)

# using an iterator for loop and built-in enumerate() function

for (idx, name) in enumerate(heroes, start =0):
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
print("Heroes = ", heroes)

import sys

try:
    sys.exit(0)

except SystemExit:
    sys.exit("Goodbye") # Explicit exit with return code (0 = success, 1-255 = error code)
