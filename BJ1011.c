#include <stdio.h>
#include <math.h>
int main() {
	int T;
	scanf("%d", &T);
	double x, y, n; //n�� �Ÿ�
	int a;
	for (int i = 0; i < T; i++)
	{
		scanf("%lf %lf", &x, &y);
		printf("y = %lf\n", y);
		printf("x = %lf\n", x);
		n = y - x;//45 50 �̵� 0 5�̵� ���� �̵� ��ġ �۵� Ƚ��
				  //���� ���� 
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