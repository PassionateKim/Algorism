#include <stdio.h>
#include <string.h> //���ڿ� ���� 

int main() {


    char Input_char[1000000];
    int Alphabet[52]; //ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz --> �׷��� ���ڸ� ���� ���̹Ƿ� int�� 
    int len = 0; //input_char �Ǳ���

    for (int i = 0; i < 52; i++) //Alphabet �迭 �μ� 0���� ��� �ʱ�ȭ 
    {
        Alphabet[i] = 0;
    }

    //---------(1)scanf�� �Է°��� �ް� �̸� ���ڿ� �迭�� �ִ´�.--------------
    scanf("%s", Input_char); //Mississipi
    len = strlen(Input_char);

    //------(2)���ڿ� �迭�� ù �ε������� for ������ üũ�ϰ� ������ ���ĺ� �迭�� �ִ´�.--------
    for (int i = 0; i < len; i++)
    {

        for (int j = 65; j <= 90; j++) //�빮�� ���Ĺ� ASCII �ڵ� A���� ~Z���� 
        {
            if (Input_char[i] == j) //M 
            {
                Alphabet[j - 65] = Alphabet[j - 65] + 1; //M = 72 �̰� Alpha�迭���� M = 13����
            }
        }

        for (int j = 97; j <= 122; j++) //�ҹ��� ���Ĺ� ASCII �ڵ� a~z���� 
        {
            if (Input_char[i] == j) //M 
            {
                Alphabet[j - 71] = Alphabet[j - 71] + 1; //i = 105 �ϋ� Alpha�迭���� 35���� 

            }
        }

    }
    //-------(3)-1 �빮�ڷ� ����ϱ�------
    for (int k = 0; k <= 25; k++) //�ҹ��ڿ� �ִ� ���� �빮�ڷ� �Ű��ֱ� 
    {
        Alphabet[k] = Alphabet[k] + Alphabet[k + 26];
    }

    for (int k = 0; k <= 25; k++)// �ҹ��� �ʱ�ȭ
    {
        Alphabet[k + 26] = 0;
    }

    int Max = Alphabet[0]; //�ִ밪
    int A = 0; //Max ���� ������ Alpha�迭�� �ε��� �� 
    for (int i = 0; i < 26; i++) //max��  ���ϱ� 
    {
        if (Alphabet[i] > Max)
        {
            Max = Alphabet[i];
            A = i;
        }
    }


    //-----------(3)-2 ������ �����ϴ� ��� ? ����ϱ�-------------
    int cnt = 0;
    for (int i = 0; i < 26; i++) //Max ���� üũ 
    {
        if (Alphabet[i] == Max)
        {
            cnt++;
        }
    }


    if (cnt > 1)
    {
        printf("?");
    }

    else
    {
        printf("%c", A + 65);
    }


    return 0;
}