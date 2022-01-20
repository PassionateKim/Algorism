#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int input_N; //주어지는 N의 값 
	int i = 1; // 사이클의 길이
	int NEW; // 새로 만들어지는 수 
	int a; //좌변의 우측 숫자
	int b; // 좌변의 좌측 숫자


	scanf("%d", &input_N); //input이 26인 경우
	a = input_N / 10;// 좌변의 왼쪽 수 대입 식 2
	b = input_N % 10; // 좌변의 오른쪽 수 대입 식 6
	NEW = a + b; // 8

	while (i) {
		printf("input_N: %d\n", input_N);
		printf("좌변의 왼쪽수 : %d\n", a);
		printf("좌변의 오른쪽수 : %d\n", b);
		printf("우변의 값 : %d\n", NEW);

		a = b;// b = 6
		b = NEW % 10; //8
		NEW = a + b; // 우변의 값   NEW =8 ,14 , 12 ,6 



		printf("-----------------------------------------");


		printf("i = %d\n", i);

		++i;

		if (input_N == (10 * a + b)) {

			break;
		}

	}

	return 0;
}
