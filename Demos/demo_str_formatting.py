#! /usr/bin/env python3
# Author: SWilliams
# Description: This script will demo
"""
    Docstring:
"""
# Dictionary of planet names and their distance to the SUN in Giga metree!
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# Iterate through the keys in the planets and display planet names
# and distance to sun USING..
# 1. ITERATOR loop plus str concatenation and escape chars - UGLY!
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm\t" + str(hex(0xff)))

print("-" * 60)
# 2. ITERATOR loop plus str concatenation and str justification methods - OK!
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12) + " Gm" + str(hex(0xff)).rjust(6))

print("-" * 60)
# 3. ITERATOR loop plus str.format() method - GOOD!
for planet in planets.keys():
    print("{0:>12s}: {1:>12.3f} Gm{2:>#6x}".format(planet, planets[planet], 0xff))

print("-" * 60)
# 3. ITERATOR loop plus f-strings (Python 3.5 onwards) - My favourite!
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:>12.3f} Gm{0xff:>#6x}")

