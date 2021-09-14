#include <stdio.h>


int main()
{

	int C; //테스트케이스
	int N; //학생수 

	printf(" -----평균은 넘겠지-----\n");

	printf("Test case 입력하시오\n");
	scanf("%d", &C);

	//--Test case 'for'--
	for (int i = 0; i < C; i++) {
		float arr[1000];
		float a = 0; //float 를 0으로 초기화해도 상관없음 아라서 0.0000이 됨
		float b = 0;
		printf("학생수를 입력하시오\n");
		scanf("%d", &N);

		printf("점수를 입력하시오\n");
		//--N안의 for 문--
		//입력받고 평균 구하기
		for (int j = 0; j < N; j++) {


			scanf("%f", &arr[j]); //점수입력받고

			a = a + arr[j] / N; //평균 구하기

		}


		// 평균 넘는 학생 수 구하기
		for (int k = 0; k < N; k++) {

			if (arr[k] > a) {


				b = b + 1;

			}

		}

		printf(" 평균 넘는 학생 수의 비율: %.3%%f\n", 100 * (b / N));


		//평균 넘는 학생 수 비율 출력하기


	}
	return 0;
}