#include <stdio.h>
#include <math.h>

int main(){
  float radius;
  float step_1;
  float step_2;
  float step_3;
  float step_4;

  printf("Enter circle radius: ");
  scanf("%f", &radius);

  // for area
  step_1 = 2 * M_PI;
  step_2 = radius * radius;
  step_3 = step_1 * step_2;
  printf("\tThe area of the circle is: %f\n", step_3);

  // for circumference
  step_4 = step_1 * radius;
  printf("\tThe circumference of the circle is: %f\n", step_4);
  return 0;
}

/*
Output:

Enter circle radius: 3.5
	The area of the circle is: 76.969025
	The circumference of the circle is: 21.991150
*/
