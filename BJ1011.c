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
		printf("y = %lf\n", y);
		printf("x = %lf\n", x);
		n = y - x;//45 50 이든 0 5이든 공간 이동 장치 작동 횟수
				  //차이 없음 
		printf("n = %lf\n", n);
		a = (int)sqrt(n);
		printf("a = %d\n", a);

		if ((int)(n) == a * a)
		{
			printf("%d\n", 2 * a - 1);
		}
	}
	return 0;
}