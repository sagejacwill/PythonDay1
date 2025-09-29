#! /usr/bin/env python3
# Author: SWilliams
# Description: This script will generate 6 UNIQUE random lottery numbers
"""
    Docstring:
"""

import random
lotto = [] #Create empty list

while len(lotto) < 6:
    num = random.randint(1, 50)
    if num in lotto:
        print("The number is already in lotto")
    else:
        lotto.append(num)

print(lotto)



