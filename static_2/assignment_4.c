#include <stdio.h>

int main(){
  int a, b;
  int c; // we use this variable to briefly store a value

  printf("Enter first number: ");
  scanf("%d", &a);

  printf("Enter second number: ");
  scanf("%d", &b);

  printf("\nYou entered `%d, %d` (a and b) respectively\n", a, b);
  printf("Values before swap are:\n\ta = %d\n\tb = %d\n", a, b);

  // swapping numbers of `a` and `b`
  a = a + b;
  b = a - b;
  a = a - b;

  // c = a;
  // a = b;
  // b = c;
  
  printf("Values after swap are:\n\ta = %d\n\tb = %d\n", a, b);

  return 0;
}

/*
Output:

Enter first number: 230
Enter second number: 780

You entered `230, 780` (a and b) respectively
Values before swap are:
	a = 230
	b = 780
Values after swap are:
	a = 780
	b = 230

*/
