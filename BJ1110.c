#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int input_N; //�־����� N�� �� 
	int i = 1; // ����Ŭ�� ����
	int NEW; // ���� ��������� �� 
	int a; //�º��� ���� ����
	int b; // �º��� ���� ����


	scanf("%d", &input_N); //input�� 26�� ���
	a = input_N / 10;// �º��� ���� �� ���� �� 2
	b = input_N % 10; // �º��� ������ �� ���� �� 6
	NEW = a + b; // 8

	while (i) {
		printf("input_N: %d\n", input_N);
		printf("�º��� ���ʼ� : %d\n", a);
		printf("�º��� �����ʼ� : %d\n", b);
		printf("�캯�� �� : %d\n", NEW);

		a = b;// b = 6
		b = NEW % 10; //8
		NEW = a + b; // �캯�� ��   NEW =8 ,14 , 12 ,6 



		printf("-----------------------------------------");


		printf("i = %d\n", i);

		++i;

		if (input_N == (10 * a + b)) {

			break;
		}

	}

	return 0;
}