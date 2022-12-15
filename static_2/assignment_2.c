#include <stdio.h>

int main(){
  float step_1;
  float step_2;
  float step_3;
  float Tf; // Tf means temprature in fahrenheit

  printf("Enter temprature scale in fahrenheit: ");
  scanf("%f", &Tf);
  // 32 degree fahrenheit is equal to 0 degree celsius

  step_1 = Tf - 32; // minusing 32 from temprature-in-fahrenheit
  step_2 = step_1 * 5; // timesing `step_1` with 5
  step_3 = step_2 / 9; // dividing `step_2` with 9
  
  printf("The conversion of %f fahrenheit to celsius is:\n\t%f celsius degree\n", Tf, step_3);
  return 0;
}


/*
Output:

Enter temprature scale in fahrenheit: 68.3
The conversion of 68.300003 fahrenheit to celsius is:
	20.166668 celsius degree
*/
