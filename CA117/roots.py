#!/usr/bin/env python3

import sys
import math

def find_roots(a, b, c):
    try:
        square = math.sqrt(int(b)**2 - 4 * int(a) * int(c))
    except ValueError:
        return None, None
    root1 = (- int(b) - square) / (2 * int(a))
    root2 = (- int(b) + square) / (2 * int(a))
    return root1, root2

for line in sys.stdin:
    tokens = line.strip().split()
    root1, root2 = find_roots(tokens[0], tokens[1], tokens[2])
    if root1 == None:
        print(None)
    else:
        print(f"{root1:.1f}, {root2:.1f}")
