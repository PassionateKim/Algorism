#include <stdio.h>



int main()
{
	float arr[999]; //길이 1000으로 default (float 인자)

	int Sub_num; //시험 본 과목의 개수 

	float Avrg = 0; //평균 (float 인자)  

	scanf("%d", &Sub_num);

	for (int i = 0; i < Sub_num; i++) {

		scanf("%f", &arr[i]);

	}
	// 여기까지하면 , 배열의 인자에 각각의 점수가 대입된다.


	//▼ 배열안의 최대값 구하기
	float max = 0;

	for (int j = 0; j < Sub_num; j++) {


		if (arr[j] > max) {
			max = arr[j];
		}


	}

	//averge 구하기 
	float a = 0;


	for (int k = 0; k < Sub_num; k++) {
		a = (arr[k] * 100) / max;
		Avrg = Avrg + a / Sub_num; // a = {(40 + 80 + 60)*100}/80
								// a/Sub_num = 225/3 =75
	}

	printf("%f\n", Avrg);

	return 0;

}