#!/usr/bin/env python3

import sys

inp = sys.stdin.readlines()
nums = {}
lines = []
num = []

i = 0

while i < len(inp):
  if inp[i].rstrip() not in nums:
    nums[inp[i].rstrip()] = 0
    num.append(int(inp[i].rstrip()))
  nums[inp[i].rstrip()] += 1
  i = i + 1

i = 0
max = 0

while i < len(num):
  curr = nums[str(num[i])]
  if curr > max:
    max = curr
  i = i + 1

i = 0

while i < max:
  line = [" | "]
  j = 0
  while j < 20:
    if str(j) in nums and nums[str(j)] > 0:
      line.append("*")
      nums[str(j)] -= 1
    else:
      line.append(" ")
    j = j + 1
  lines.append("".join(line))
  i = i + 1

i = len(lines) - 1

while i > -1:
  print(lines[i].rstrip())
  i = i - 1

print(" " + "-" * 23)
