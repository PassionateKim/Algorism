#include <stdio.h>


int main()
{
    int arr[10]; //�Է¹��� 10���� ���� ���� 42�� ���� �������� ������ �迭 ����


    int Different_remain = 0;

    printf("----------42�� ���� ������ ����\n");
    printf("10���� ���� �Է��Ͻÿ�\n");

    for (int i = 0; i <= 9; i++) {

        scanf("%d", &arr[i]);
        arr[i] = arr[i] % 42; // �Է� ������ ������

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