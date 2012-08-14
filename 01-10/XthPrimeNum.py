#!/usr/bin/python3
def main():
  x = 10001
  primecount = 0
  count = 2
  while ( primecount < x ):
    if ( isPrime(count) != -1 ):
      primecount +=1
      print("prime #{} - {}".format(primecount, count))
    count += 1
#  print(count-1)

def isPrime(num):
  divs = 0
  for elem in range (1, num+1):
    if (num % elem) == 0:
      divs += 1
      if (divs > 2):
        return -1;
  return 0

main()
