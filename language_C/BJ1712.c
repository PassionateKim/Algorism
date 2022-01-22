#include <stdio.h>

int main() {

	int A, B, C;
	scanf("%d %d %d", &A, &B, &C);

	int x = 1;

	if (B >= C) {
		printf("-1");
	}

	else// C>B ÀÎ °æ¿ì
	{
		x = A / (C - B);
		printf("%d", (int)x + 1);
	}

	
	return 0;
}
