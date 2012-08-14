#include<stdio.h>
main() {
  int i=20, x=1;

  while (x != 0) {
    i += 20;
    //printf("i=%d\n", i);
    if (isDivisibleTest(i) == 0){
      printf("smallest number divisible by every number 1-20 = %d\n", i);
      break;
    }
  }
  return 0;
}


isDivisibleTest(int x) {
  int i;
  for (i=1; i<21; i++) {
    if (x%i != 0) {
      return -1;
    }
  }
  return 0;
}
