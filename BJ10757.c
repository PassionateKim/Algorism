#include <stdio.h>
#include <string.h>

void reverse(char arr[]) //���ڿ� ���� ����
{
	int len = strlen(arr);
	for (int i = 0; i < len / 2; i++) 
	{
		char temp = arr[i];
		arr[i] = arr[len - i - 1];
		arr[len - i - 1] = temp;
	}
}


int main() {
	char A[10002] = { 0 };
	char B[10002] = { 0 };
	char res[10003] = { 0 };
	int carry = 0; //�ڸ��� �ø�
	int len = 0;
	scanf("%s %s", A, B);

	reverse(A);
	reverse(B);

	if (strlen(A) > strlen(B)) //ū�� ���� 
	{
		len = strlen(A);
	}
	else
	{
		len = strlen(B);
	}

	for (int i = 0; i < len; i++)
	{
		int sum = A[i] - '0' + B[i] - '0' + carry; //ASCII �ڵ� ���� ������ ��
		if (sum < 0)//�ڸ����� �ٸ����(sum < 0) sum�� -'0'�� �ѹ� �� ����
		{
			sum += '0';//�׷���� +'0'�� �ؼ� �����ش�.
		}
		if (sum > 9)
		{
			carry = 1; //���Ѱ��� 9�� �Ѿ�� �� �����ڸ��� +1 ������ϹǷ�
		}
		else
		{
			carry = 0;
		}
		res[i] = sum % 10 +'0';
	}
	if (carry == 1)//�������ڸ��� sum�� 9�� ������ �ڸ����� �ϳ� �� Ŀ���Ƿ� 
	{
		res[len] = '1';
	}
	reverse(res);
	printf("%s", res);
	return 0;
}