#include <stdio.h>
int main() {

	int a = 0;
	int b = 0;
	int T = 0; //test case 
	int numArr[15][15] = { 0, };

	//기초배열채우기
	for (int j = 0; j < 15; j++) //맨 아랫줄
	{
		numArr[0][j] = j + 1;
	}
	for (int i = 0; i < 15; i++) //맨 왼쪽줄
	{
		numArr[i][0] = 1;
	}

	for (int i = 1; i < 15; i++)
	{
		for (int j = 1; j < 15; j++)
		{
			numArr[i][j] = numArr[i - 1][j] + numArr[i][j - 1];
		}
	}


	for (int i = 0; i < 15; i++) //배열 체크하기
	{
		for (int j = 0; j < 15; j++)
		{
			printf("%8d ", numArr[i][j]);
		}
		printf("\n");
	}


	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &a);
		scanf("%d", &b);
		printf("%d\n", numArr[a][b - 1]);
	}

	return 0;
}