#!/usr/bin/python3

a = 0
b = 0
c = 0

for a in range(1, 1000):
  for b in range(1, 1000):
    c = 1000 - b - a
    if a*a + b*b == c*c:
      print(a*b*c)
