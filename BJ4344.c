#include <stdio.h>


int main()
{

	int C; //�׽�Ʈ���̽�
	int N; //�л��� 

	printf(" -----����� �Ѱ���-----\n");

	printf("Test case �Է��Ͻÿ�\n");
	scanf("%d", &C);

	//--Test case 'for'--
	for (int i = 0; i < C; i++) {
		float arr[1000];
		float a = 0; //float �� 0���� �ʱ�ȭ�ص� ������� �ƶ� 0.0000�� ��
		float b = 0;
		printf("�л����� �Է��Ͻÿ�\n");
		scanf("%d", &N);

		printf("������ �Է��Ͻÿ�\n");
		//--N���� for ��--
		//�Է¹ް� ��� ���ϱ�
		for (int j = 0; j < N; j++) {


			scanf("%f", &arr[j]); //�����Է¹ް�

			a = a + arr[j] / N; //��� ���ϱ�

		}


		// ��� �Ѵ� �л� �� ���ϱ�
		for (int k = 0; k < N; k++) {

			if (arr[k] > a) {


				b = b + 1;

			}

		}

		printf(" ��� �Ѵ� �л� ���� ����: %.3%%f\n", 100 * (b / N));


		//��� �Ѵ� �л� �� ���� ����ϱ�


	}
	return 0;
}