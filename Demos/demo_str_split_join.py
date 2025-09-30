#! /usr/bin/env python3
# Author: SWilliams
# Description: This script will demo
"""
    Docstring:
"""

# Sample line from /etc/passwd in Linux for the root user account

line = "root:x:0:0:The Super User:/root:/bin/bash"

fields = line.split(":")
fields[4] = "The Administrator"
fields[6] = "/bin/zsh"

line = ":".join(fields)
print("Modified str =", line)

