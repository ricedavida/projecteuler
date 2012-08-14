#include<stdio.h>
main() {
 int diff;
 diff =squareOfSums(100) - sumOfSquares(100);
 printf("diff = %d\n", diff);

 return 0;
}

sumOfSquares(int x) {
  int i, sum=0;
  for (i=1; i<x+1; i++) {
    sum = (i*i) + sum;
  }
  return sum;
}

squareOfSums(int x) {
  int i, sum=0;
  for (i=1; i<x+1; i++) {
    sum = sum + i;
  }
  return (sum * sum);
}
