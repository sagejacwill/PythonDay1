#! /usr/bin/env python3
# Author: SWilliams
# Description: This script will demo
"""
    Docstring:
"""

def search_word(pattern=r"sage", *files):
    lines_matched = 0
    for file in files:
        with (open(file, mode="rt") as fh_in):
            for (line_num, line) in enumerate(fh_in, start=1):
                if line.isascii() and pattern in line:
                    print(line_num, line, end="")
                    lines_matched += 1
    return lines_matched

total_lines = 0
total_lines += search_word("arash", "words", "words", "words")
print("-" * 50)
total_lines += search_word()
print("-" * 50)
print(f"Total lines matched = {total_lines}")