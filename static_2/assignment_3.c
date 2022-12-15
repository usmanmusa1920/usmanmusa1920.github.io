#include <stdio.h>
 
#define MAXROW 10
#define MAXCOL 10

int main(){
  int matrix[MAXROW][MAXCOL];
  int i, j;
  int m = 3, n = 3;

  printf("\nEnter matrix elements :\n");
  for(i = 0; i < m; i++){
    for(j = 0; j < n; j++){
      printf("Enter element of row %d column %d [%d, %d] : ",i + 1, j + 1, i + 1, j + 1);
      scanf("%d", &matrix[i][j]);
    }
  }

  printf("\nThe matrix is :\n");
  for(i = 0; i < m; i++){
    for(j = 0; j < n; j++){
      printf("%d\t", matrix[i][j]);
    }
    printf("\n"); // new line after row elements
  }
  return 0;
}

/*
Output:

Enter matrix elements :
Enter element of row 1 column 1 [1, 1] : 5
Enter element of row 1 column 2 [1, 2] : 7
Enter element of row 1 column 3 [1, 3] : 3
Enter element of row 2 column 1 [2, 1] : 9
Enter element of row 2 column 2 [2, 2] : 4
Enter element of row 2 column 3 [2, 3] : 2
Enter element of row 3 column 1 [3, 1] : 0
Enter element of row 3 column 2 [3, 2] : 6
Enter element of row 3 column 3 [3, 3] : 1

The matrix is :
5	7	3	
9	4	2	
0	6	1
*/
