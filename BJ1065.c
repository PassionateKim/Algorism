#include <stdio.h>


int han_num(i) { //�Ѽ� ���ϱ� �Լ� ����
	printf("��: %d\n", i);
	int cnt = 0; //�� �ڸ� �� �� �Ѽ� �ΰ��� �����ֱ� ���� ���� ����

	//���ڸ� ���� ��/ �ƴ� ���� �������ִ� �� 
	if (i < 100) {

		return i;
	}
	else {


		for (int j = 100; j <= i; j++) {

			int hund = j / 100;  //���� �ڸ�
			int ten = j / 10 % 10;   //�� �� �ڸ�
			int one = j % 10; //���� �ڸ�

			if (hund - ten == ten - one) {
				++cnt;
			}

		}
	}
	return (99 + cnt);
}





int main()
{
	int input, res;
	scanf("%d", &input);
	res = han_num(input);
	printf("%d", res);

	return 0;
}