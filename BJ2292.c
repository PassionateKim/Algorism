#include <stdio.h>

int main() {
	int N;
	scanf("%d", &N);
	
	for (int n =0; n*(n+1) < 1000000000; n++)
	{
		int a = 3*n*(n + 1);
		
		if (N == 1)
		{
			printf("%d", N);
			break;
		}
		if ((a + 2) <= N && N <= (a + 6*n + 7))
		{
			printf("%d", n + 2);
			break;
		}
	 
	}
	

	

	return 0;
}