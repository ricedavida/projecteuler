#include<stdio.h>
main() {
  int i, count=1, total;
  for (i=3; i<600851475144; i+=2) {
    if (isPrime(i) == 0) {
      total = i;
      count++;
    }
  }
  printf("the %d prime is %d\n", count-1, total);
  return 0;
}

isPrime(int x) {
  int i, count=0;
  for (i=0; i<x; i++) {
//    printf("in here %d\n", count+1);
    if (i%x == 0){
      count++;
    }
    if (count == 2) {
      return -1;
    }
  }
  return 0;
}
