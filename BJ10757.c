#include <stdio.h>
#include <string.h>

void reverse(char arr[]) //문자열 역순 정렬
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
	int carry = 0; //자리수 올림
	int len = 0;
	scanf("%s %s", A, B);

	reverse(A);
	reverse(B);

	if (strlen(A) > strlen(B)) //큰수 기준 
	{
		len = strlen(A);
	}
	else
	{
		len = strlen(B);
	}

	for (int i = 0; i < len; i++)
	{
		int sum = A[i] - '0' + B[i] - '0' + carry; //ASCII 코드 보며 이해할 것
		if (sum < 0)//자리수가 다를경우(sum < 0) sum은 -'0'이 한번 더 계산됨
		{
			sum += '0';//그런경우 +'0'을 해서 맞춰준다.
		}
		if (sum > 9)
		{
			carry = 1; //더한것이 9를 넘어가면 그 다음자리수 +1 해줘야하므로
		}
		else
		{
			carry = 0;
		}
		res[i] = sum % 10 +'0';
	}
	if (carry == 1)//마지막자리의 sum이 9를 넘으면 자리수가 하나 더 커지므로 
	{
		res[len] = '1';
	}
	reverse(res);
	printf("%s", res);
	return 0;
}