#include <stdio.h>


int main()
{
    int arr[10]; //입력받은 10개의 수를 각각 42로 나눈 나머지를 저장할 배열 선언


    int Different_remain = 0;

    printf("----------42로 나눈 나머지 문제\n");
    printf("10개의 수를 입력하시오\n");

    for (int i = 0; i <= 9; i++) {

        scanf("%d", &arr[i]);
        arr[i] = arr[i] % 42; // 입력 값들의 나머지

    }

    for (int j = 0; j <= 9; j++) {
        int count = 0;

        for (int k = j + 1; k <= 9; k++) {

            if (arr[j] == arr[k]) {
                ++count;
            }

        }
        if (count == 0) {
            ++Different_remain;
        }

    }

    printf("%d", Different_remain);
    return 0;

}
