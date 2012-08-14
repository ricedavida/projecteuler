#!/usr/bin/python3
def main():
  x = sum_of_sqrs(100)
  y = sqr_of_sums(100)
  print(x)
  print(y)

  print("difference is {}".format(y-x))

def sum_of_sqrs (num):
  total = 0
  for elem in range(1, num+1):
    total += elem * elem
  return total

def sqr_of_sums (num):
  total = 0
  for elem in range(1, num+1):
    total += elem
  total = total * total
  return total

main()
