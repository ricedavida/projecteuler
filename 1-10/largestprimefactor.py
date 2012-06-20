#!/usr/bin/python3
def main():
  factor = 0
  number = 600851475143
  for elem in range (1, number):
    if ((number % elem) == 0):
      if (isPrime(elem) == 0):
        #print(elem)
        factor = elem

  print(factor)

def isPrime(num):
  divs = 0
  for elem in range (1, num):
    if (num % elem) == 0:
      divs += 1
      if (divs > 2):
        return -1;
  return 0

main()
