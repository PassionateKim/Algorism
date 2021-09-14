#include <stdio.h>
#include <string.h>

int main()
{
	char input[101]; //100까지니까 char 배열 크기 100+1 = 101
	int count = 0; // 알파벳의 개수 

	//1)문자열  입력

	scanf("%s", input); // ljes=njak

	//2)알파벳 변환

	for (int i = 0; input[i] != '\0'; i++)//i=9에서 종료
	{
		if (input[i] == 'c')
		{
			if (input[i + 1] == '=' || input[i + 1] == '-')
			{
				i++;
				count++;
				continue;
			}
		}

		//3)d의 경우 case분류하기
		if (input[i] == 'd')
		{
			if (input[i + 1] == '-')
			{
				i++;
				count++;
				continue;
			}

			if (input[i + 1] == 'z')
			{
				if (input[i + 2] == '=')
				{
					i = i + 2;//인덱스 두 칸 넘어가야 하므로
					count++;
					continue;
				}

				else
				{

					count++;
					continue;

				}
			}
		}

		if (input[i] == 'l')
		{
			if (input[i + 1] == 'j')
			{
				i++;
				count++;
				continue;

			}
		}

		if (input[i] == 'n')
		{
			if (input[i + 1] == 'j')
			{
				i++;
				count++;
				continue;
			}
		}

		if (input[i] == 's')
		{
			if (input[i + 1] == '=')
			{
				i++;
				count++;
				continue;
			}
		}

		if (input[i] == 'z')
		{
			if (input[i + 1] == '=')
			{
				i++;
				count++;
				continue;
			}
			count++;
		}

		else
		{
			count++;
		}
	}
	//4) 더해서 출력 
	printf("%d", count);;
	return 0;
}