#include <stdio.h>
#include <string.h> //strtok �Լ��� ���� �� 

int main() {
	int T = 0; //TEST CASE ���� 
	char input[22]; //R+space+chleo 20���� <=22 �̹Ƿ� ���� 22�� char �� �迭 ���� 
	int M = 0;; // ������ �� 
	int cnt = 0;
	scanf("%d", &T);


	for (int i = 0; i < T; i++) {

		scanf("%d %s", &M, input);

		for (int i = 0; i < strlen(input); i++) {

			cnt = 0;
			while (cnt < M)
			{
				printf("%c", input[i]);
				cnt++;
			}

		}
		printf("\n");
	}



	return 0;

}