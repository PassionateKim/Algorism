#include <stdio.h>
#include <string.h>

int main() {

	char input[15];  //2~15 = 14�� \0�����ؼ� 15��
	int Sum = 0; // �հ� 
	int len = 0; //���ڿ��� ���� 

	//1)���ڿ��� �Է¹޴´�.
	scanf("%s", input);


	len = strlen(input); //strlen �Լ��� return�� len������



	//2)���ڿ��� �μ��� ������� Ȯ���ؼ� ���ǿ� �°� ���ڸ� ���Ѵ�.
	for (int i = 0; i < len; i++)
	{
		if (input[i] == 'A' || input[i] == 'B' || input[i] == 'C')
		{
			Sum = Sum + 3;
		}

		if (input[i] == 'D' || input[i] == 'E' || input[i] == 'F')
		{
			Sum = Sum + 4;
		}

		if (input[i] == 'G' || input[i] == 'H' || input[i] == 'I')
		{
			Sum = Sum + 5;
		}

		if (input[i] == 'J' || input[i] == 'K' || input[i] == 'L')
		{
			Sum = Sum + 6;
		}

		if (input[i] == 'M' || input[i] == 'N' || input[i] == 'O')
		{
			Sum = Sum + 7;
		}

		if (input[i] == 'P' || input[i] == 'Q' || input[i] == 'R' || input[i] == 'S')
		{
			Sum = Sum + 8;
		}

		if (input[i] == 'T' || input[i] == 'U' || input[i] == 'V')
		{
			Sum = Sum + 9;
		}

		if (input[i] == 'W' || input[i] == 'X' || input[i] == 'Y' || input[i] == 'Z')
		{
			Sum = Sum + 10;
		}

	}

	printf("%d", Sum);
	return 0;

}