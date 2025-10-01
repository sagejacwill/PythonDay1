#! /usr/bin/env python3
# Author: SWilliams
# Description: This script will demo file handling and string parsing
"""
    Docstring:
"""

try:
    with open("words", "r") as file:
        for line_num, line in enumerate(file, start=1):
            word = line.strip()
            if word.startswith("Y") or word.endswith("n") or "town" in word:
                print(f"{line_num}: {word.upper()}")

except FileNotFoundError:
    print("The file 'words' was not found. Please make sure it exists in the project directory.")

