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
		n = y - x;//45 50 �̵� 0 5�̵� ���� �̵� ��ġ �۵� Ƚ��
				  //���� ���� 
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