#!/usr/bin/python3

def isPalendrome(num):
### this function will test if the number is a palendrome, and return 0 if it is, if it is not it will return -1
  print(num)
  if (len(num) == 0):
    return 0
  if (len(num) == 1):
    return 0
  if (num[0] == num[len(num)-1]):
    return isPalendrome(num[1::-1]) 
  return -1

x = 0
for elem in range(100, 999):
  x = 999 * elem
  if isPalendrome(str(x)) == 0:
    print(str(x))
