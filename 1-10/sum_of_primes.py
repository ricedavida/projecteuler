def main():
  total = 0
  for elem in range(2, 2000000):
    if (isPrime(elem) == 0):
      total += elem
      print(elem)
  print (total)

def isPrime(num):
  divs = 0
  for elem in range (1, num+1):
    if (num % elem) == 0:
      divs += 1
      if (divs > 2):
        return -1;
  return 0

main()
