#include <stdio.h>
int main()
{
	int  N;
	scanf("%d", &N); //4
	int cnt = 0;

	if (N % 5 == 0) //아니므로 pass
	{
		cnt = cnt + N / 5;
		printf("%d", cnt);
		return 0;
	}
	else
	{
		int Q = N / 5;  //4 / 5 = 0 


		while (1)
		{
			if ((N - 5 * Q) % 3 == 0)   // 4 % 3 == 1
			{
				cnt = Q + (N - 5 * Q) / 3;
				printf("%d", cnt);
				return 0;
			}
			else
			{
				Q = Q - 1; // 
			}
			if (Q == -1) // x = 0 일 때 조차 안된 case이므로 -1
			{
				printf("-1");
				return 0;
			}
		}
	}

	return 0;
}