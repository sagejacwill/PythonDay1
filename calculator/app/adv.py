#! /usr/bin/env python3
# Author: SWilliams
# Description: This module defines advanced calc functions
"""
    Advanced Calc Module with mod, power and sqrt functions
"""

def mod(x, z):
    """ Return REMAINDER after integer div of x by z """
    return float(x%z)

def power(x, z):
    """ Return the POWER of x to z as a float """
    return float(x**z)

def sqrt(x):
    """ Return Square root of x to 3 decimal places """
    return round(x**0.5, 3)

print("########### Adv Calc Examples ############")
print(f"4 % 3 = {mod(4, 3)}")
print(f"4 ** 3 = {power(4, 3)}")
print(f"\N{square root}99 = {sqrt(99)}")
print("###########################################")