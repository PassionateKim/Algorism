#include <stdio.h>



//문자열에는 포인터를 활용하는 방법/ 배열을 활용하는 방법이 있다
// 포인터를 활용하는 방법은 scanf값을 대입해줄 수 없으므로, ( 읽기전용 )
// 배열을 활용하는 방법을 선택하기로 하였다.



int main() {

	int N; //입력할 숫자의 개수 
	char arr[100]; //크기가 100인 char 형 배열 선언
	int sum = 0; // 입력된 숫자들의 합 선언 


	scanf("%d", &N); //입력받아 N에 넣기 

	//숫자 한꺼번에 입력 by 문자열 
	scanf("%s", &arr);


	//문자형을 정수형으로 변환해준 뒤, atoi함수 활용
	// 정수형 끼리 더해서 출력 
	for (int i = 0; i < N; i++) {

		sum = sum + arr[i] - '0';

	}
	printf("%d", sum);

	return 0;
}