#include<stdio.h>

int main() {

	int A, B, C; //�Է°� A , B , C 
	int Total; // A * B * C

	int arr0 = 0; //�迭�� 0��° , 0���� �ʱ�ȭ
	int arr1 = 0; //�迭�� 1��° , 0���� �ʱ�ȭ
	int arr2 = 0; //�迭�� 2��° , 0���� �ʱ�ȭ
	int arr3 = 0; //�迭�� 3��° , 0���� �ʱ�ȭ
	int arr4 = 0; //�迭�� 4��° , 0���� �ʱ�ȭ
	int arr5 = 0; //�迭�� 5��° , 0���� �ʱ�ȭ
	int arr6 = 0; //�迭�� 6��° , 0���� �ʱ�ȭ
	int arr7 = 0; //�迭�� 7��° , 0���� �ʱ�ȭ
	int arr8 = 0; //�迭�� 8��° , 0���� �ʱ�ȭ
	int arr9 = 0; //�迭�� 9��° , 0���� �ʱ�ȭ

	int arr[10]; //�迭 ����

	scanf("%d", &A);
	scanf("%d", &B);
	scanf("%d", &C);

	Total = A * B * C;



	while (Total > 0)
	{

		if (Total % 10 == 0)
		{

			Total = Total / 10;

			++arr0;
		}


		if (Total % 10 == 1)
		{

			Total = Total / 10;

			++arr1;
		}

		if (Total % 10 == 2)
		{

			Total = Total / 10;

			++arr2;
		}

		if (Total % 10 == 3)
		{

			Total = Total / 10;

			++arr3;
		}

		if (Total % 10 == 4)
		{

			Total = Total / 10;

			++arr4;
		}

		if (Total % 10 == 5)
		{

			Total = Total / 10;

			++arr5;
		}

		if (Total % 10 == 6)
		{

			Total = Total / 10;

			++arr6;
		}

		if (Total % 10 == 7)
		{

			Total = Total / 10;

			++arr7;
		}

		if (Total % 10 == 8)
		{

			Total = Total / 10;

			++arr8;
		}

		if (Total % 10 == 9)
		{

			Total = Total / 10;


			++arr9;
		}

		arr[0] = arr0;
		arr[1] = arr1;
		arr[2] = arr2;
		arr[3] = arr3;
		arr[4] = arr4;
		arr[5] = arr5;
		arr[6] = arr6;
		arr[7] = arr7;
		arr[8] = arr8;
		arr[9] = arr9;


	}
	for (int i = 0; i <= 9; i++) {

		printf("%d\n", arr[i]);

	}
	return 0;
}