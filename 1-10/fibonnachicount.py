#!/usr/bin/python3
fcur = 0
fmin1 = 2
fmin2 = 1
count = 2

while( fcur < 4000000 ):
  fcur = fmin1 + fmin2
  print(fcur)  
  if (fcur % 2) == 0:
    count += fcur
  
  fmin2 = fmin1
  fmin1 = fcur

print (count)
