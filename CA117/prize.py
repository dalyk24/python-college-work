#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()
cups = [False, False, False]

cups[int(inp[0]) - 1] = True
swaps = [s for s in inp[1].strip()]

for s in swaps:
	if s == "A":
		temp = cups[0]
		cups[0] = cups[1]
		cups[1] = temp
	elif s == "B":
		temp = cups[1]
		cups[1] = cups[2]
		cups[2] = temp
	elif s == "C":
		temp = cups[0]
		cups[0] = cups[2]
		cups[2] = temp

print(cups.index(True) + 1)
