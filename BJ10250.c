#include <stdio.h>
#include  <math.h>

int main() {

	int T;
	scanf("%d",&T);

	for (int i = 0; i < T; i++)
	{
		int H, W, N;
		int floor; //Ãþ
		int room_num; //È£¼ö
		scanf("%d %d %d", &H, &W, &N);
		if ((N % H) == 0)
		{
			floor = H;
			room_num = (N / H);
		}
		else
		{
			floor = (N % H);
			room_num = (N / H) + 1;
		}

		if (room_num < 10)
		{
			printf("%d", floor);
			printf("0");
			printf("%d", room_num);
			printf("\n");
		}
		else
		{
			printf("%d", floor);
			printf("%d", room_num);
			printf("\n");
		}
		
	}
	return 0;
}