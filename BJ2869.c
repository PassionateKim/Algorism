#include <stdio.h>
#include  <math.h>
int main() {
	int A, B, V;
	
	scanf("%d %d %d", &A, &B, &V);
	
	
if (A == V)
{
	printf("1");
	return 0;
}

else
{
	(V - A) / (A - B);
	int x = V - A;
	int y = A - B;
	int a = ceil((double)x / (double)y);
	printf("%d", a+1);
	
}

	return 0;
}