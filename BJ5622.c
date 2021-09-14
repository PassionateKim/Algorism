#include <stdio.h>
#include <string.h>

int main() {

	char input[15];  //2~15 = 14개 \0까지해서 15개
	int Sum = 0; // 합계 
	int len = 0; //문자열의 길이 

	//1)문자열을 입력받는다.
	scanf("%s", input);


	len = strlen(input); //strlen 함수의 return을 len변수에



	//2)문자열의 인수를 순서대로 확인해서 조건에 맞게 숫자를 더한다.
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