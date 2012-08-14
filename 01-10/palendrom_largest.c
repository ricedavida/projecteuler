#include<stdio.h>

main() {
  int x=0, bigx=0, var1=0, var2=0, i, j;
  for (i=100; i<1000; i++) {
    for (j=100; j<1000; j++) {
      x = i * j;
      if (isPalendrome(x) == 0) {
        if (bigx < x) {
          bigx = x;
          var1 = i;
          var2 = j;
        }
      }
    }
  }
  printf("The largest palendrome is: %d\n", bigx);
  printf("The two numbers are %d & %d", var1, var2);
}

isPalendrome(int x) {
  int y = x;
  int mod, rev=0;
  while ( x > 0 ) {
    mod = x%10;
    rev = rev*10 + mod;
    x = x/10;
  }
  if (y == rev) {
    return 0;
  }
  else 
    return 1;
}

