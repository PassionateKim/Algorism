#include <stdio.h>
#include <string.h>

int main()
{
	char input[101]; //100�����ϱ� char �迭 ũ�� 100+1 = 101
	int count = 0; // ���ĺ��� ���� 

	//1)���ڿ�  �Է�

	scanf("%s", input); // ljes=njak

	//2)���ĺ� ��ȯ

	for (int i = 0; input[i] != '\0'; i++)//i=9���� ����
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

		//3)d�� ��� case�з��ϱ�
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
					i = i + 2;//�ε��� �� ĭ �Ѿ�� �ϹǷ�
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
	//4) ���ؼ� ��� 
	printf("%d", count);;
	return 0;
}