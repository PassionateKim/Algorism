#include <stdio.h>
#include <string.h>    // strlen �Լ��� ����� ��� ����


int main()
{
	int Test_case;


	//Testcase �� ���� �Է�
	printf("Testcase�� ������ �Է��Ͻÿ�\n");
	scanf("%d", &Test_case);

	int count;
	int total;
	//���ڿ��� 0���� ũ�� 80���� �����Ƿ� 
	char score[79]; //���ڿ� �������� �迭 ���� (0~79)

	for (int i = 0; i < Test_case; i++) {

		total = 0;
		count = 1; //���⼭ �ʱ�ȭ�� ���־�� ���� ����Ŭ�� ������ ���� �ʴ´� 


		printf("�Է�:");
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