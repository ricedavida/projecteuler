#!/usr/bin/python3
x = 0

for elem in range(0, 1000):
  if ((elem % 3) == 0):
    x += elem
    print (elem)
  elif ((elem % 5) == 0):
    x += elem
    print(elem)

print(x)

