#include <stdio.h>
#include <string.h>    // strlen 함수가 선언된 헤더 파일


int main()
{
	int Test_case;


	//Testcase 의 개수 입력
	printf("Testcase의 개수를 입력하시오\n");
	scanf("%d", &Test_case);

	int count;
	int total;
	//문자열은 0보다 크고 80보다 작으므로 
	char score[79]; //문자열 형식으로 배열 선언 (0~79)

	for (int i = 0; i < Test_case; i++) {

		total = 0;
		count = 1; //여기서 초기화를 해주어야 다음 싸이클에 영향을 주지 않는다 


		printf("입력:");
		scanf("%s", score);


		//score = "OXOXOX"
		for (int j = 0; j < strlen(score); j++) {



			if (score[j] == 'O') {

				total = total + count;
				++count;

				printf("total: %d\n", total);
			}

			if (score[j] == 'X') {

				count = 1;
				printf("----------count = 1\n");
			}


		}

		printf("%d\n", total);

	}
	return 0;

}