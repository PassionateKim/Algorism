#include <stdio.h>



int main()
{
	float arr[999]; //���� 1000���� default (float ����)

	int Sub_num; //���� �� ������ ���� 

	float Avrg = 0; //��� (float ����)  

	scanf("%d", &Sub_num);

	for (int i = 0; i < Sub_num; i++) {

		scanf("%f", &arr[i]);

	}
	// ��������ϸ� , �迭�� ���ڿ� ������ ������ ���Եȴ�.


	//�� �迭���� �ִ밪 ���ϱ�
	float max = 0;

	for (int j = 0; j < Sub_num; j++) {


		if (arr[j] > max) {
			max = arr[j];
		}


	}

	//averge ���ϱ� 
	float a = 0;


	for (int k = 0; k < Sub_num; k++) {
		a = (arr[k] * 100) / max;
		Avrg = Avrg + a / Sub_num; // a = {(40 + 80 + 60)*100}/80
								// a/Sub_num = 225/3 =75
	}

	printf("%f\n", Avrg);

	return 0;

}