#! /usr/bin/env python3
# Description: This script is a VERY Basic Calculator App with few functions!
# Comments for the developer/coder

"""
    Basic Calculator App with add, multiply and divide features
"""

import sys

def add(*args):
    """ Return SUM of all arguments as a float """
    sum = 0
    for num in args:
        sum += num
    return float(sum)

def mul(*args):
    """ Return PRODUCT of all arguments as a float """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return QUOTIENT of x divided by z to 3 decimal places """
    return round(x/z, 3)

def main():
    print("----------- Basic Calc Examples ------------")
    print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    print("--------------------------------------------")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
