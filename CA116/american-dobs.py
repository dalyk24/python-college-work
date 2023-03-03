#!/usr/bin/env python3

with open("irish-dobs.txt") as f:
  dobs = f.readlines()

i = 0
j = 0
with open("american-dobs.txt", "w") as f:
  while i < len(dobs):
    tokens = dobs[i].split("/")
    day = tokens[0]
    month = tokens[1].split("/")
    year_name = tokens[2].split(" ")
    date = month[0], day, year_name[0]
    date = "/".join(date) + " " + " ".join(year_name[1:])
    f.write(date)
    i = i + 1
