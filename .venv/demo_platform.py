#! /usr/bin/env python3
# Author: SWilliams
# Description: This script will demo
"""
    Docstring:
"""

import sys
import os

my_home = None

if sys.platform == "win32":
    my_home = os.environ['HOMEPATH']
elif sys.platform == "darwin" or sys.platform == "linux":
    my_home = os.environ['HOME']
else:
    print("Other OS")

print("Home is", my_home)

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
    else:
        print("Invalid PIN")
        attempts += 1
else:
    print("Maximum attempts reached")




