#include <stdio.h>
#include <math.h>
int main() {
	int T;
	scanf("%d", &T);
	double x, y, n; //n은 거리
	int a;
	for (int i = 0; i < T; i++)
	{
		scanf("%lf %lf", &x, &y);
		n = y - x;//45 50 이든 0 5이든 공간 이동 장치 작동 횟수
				  //차이 없음 
		a = (int)sqrt(n);

		if ((int)(n) == a * a)
		{
			printf("%d\n", 2 * a - 1);
		}
		else if ((int)(n) > a * a && (int)n <= a * a + a)//9<n<=12
		{
			printf("%d\n", 2 * a);
		}
		else
		{
			printf("%d\n", 2 * a + 1);
		}
	}
	return 0;
}
