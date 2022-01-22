#include <stdio.h>
#include <string.h> //strtok 함수를 위한 것 

int main() {
	int T = 0; //TEST CASE 개수 
	char input[22]; //R+space+chleo 20글자 <=22 이므로 길이 22인 char 형 배열 선언 
	int M = 0;; // 좌측의 수 
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
