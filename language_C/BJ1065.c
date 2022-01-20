#include <stdio.h>


int han_num(i) { //한수 구하기 함수 생성
	printf("수: %d\n", i);
	int cnt = 0; //세 자리 수 중 한수 인것을 더해주기 위한 변수 선언

	//세자리 수일 / 아닐 때로 구분해주는 식 
	if (i < 100) {

		return i;
	}
	else {


		for (int j = 100; j <= i; j++) {

			int hund = j / 100;  //백의 자리
			int ten = j / 10 % 10;   //십 의 자리
			int one = j % 10; //일의 자리

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
