#!/usr/bin/python3

def isPalendrome(num):
### this function will test if the number is a palendrome, and return 0 if it is, if it is not it will return -1
  if (len(num) == 0):
    return 0
  if (len(num) == 1):
    return 0
  if (num[0] == num[len(num)-1]):
    return isPalendrome(num[1:-1]) 
  return -1

x = 0
bigx = 0
var1 = 0
var2 = 0
for elem in range(100, 999):
  for subelem in range(100, 999):
    x = subelem * elem
    if isPalendrome(str(x)) == 0:
      if (bigx < x):
        bigx = x
        var1 = elem
        var2 = subelem
print("The largest palendrome you can make by multiplying two, three digit numbers together is {}, and the two numbers are {} * {}.".format(bigx, var1, var2))

#x = isPalendrome("hannah")
#print (x)
