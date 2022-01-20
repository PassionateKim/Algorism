#include <stdio.h>
#include <string.h> //문자열 길이 

int main() {


    char Input_char[1000000];
    int Alphabet[52]; //ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz --> 그러나 숫자만 넣을 것이므로 int형 
    int len = 0; //input_char 의길이

    for (int i = 0; i < 52; i++) //Alphabet 배열 인수 0으로 모두 초기화 
    {
        Alphabet[i] = 0;
    }

    //---------(1)scanf에 입력값을 받고 이를 문자열 배열에 넣는다.--------------
    scanf("%s", Input_char); //Mississipi
    len = strlen(Input_char);

    //------(2)문자열 배열을 첫 인덱스부터 for 문으로 체크하고 개수를 알파벳 배열에 넣는다.--------
    for (int i = 0; i < len; i++)
    {

        for (int j = 65; j <= 90; j++) //대문자 알파뱃 ASCII 코드 A부터 ~Z까지 
        {
            if (Input_char[i] == j) //M 
            {
                Alphabet[j - 65] = Alphabet[j - 65] + 1; //M = 72 이고 Alpha배열에서 M = 13번
            }
        }

        for (int j = 97; j <= 122; j++) //소문자 알파뱃 ASCII 코드 a~z까지 
        {
            if (Input_char[i] == j) //M 
            {
                Alphabet[j - 71] = Alphabet[j - 71] + 1; //i = 105 일 Alpha배열에서 35번 

            }
        }

    }
    //-------(3)-1 대문자로 출력하기------
    for (int k = 0; k <= 25; k++) //소문자에 있던 것을 대문자로 옮겨주기 
    {
        Alphabet[k] = Alphabet[k] + Alphabet[k + 26];
    }

    for (int k = 0; k <= 25; k++)// 소문자 초기화
    {
        Alphabet[k + 26] = 0;
    }

    int Max = Alphabet[0]; //최대값
    int A = 0; //Max 값을 가지는 Alpha배열의 인덱스 값 
    for (int i = 0; i < 26; i++) //max값  구하기 
    {
        if (Alphabet[i] > Max)
        {
            Max = Alphabet[i];
            A = i;
        }
    }


    //-----------(3)-2 여러개 존재하는 경우 ? 출력하기-------------
    int cnt = 0;
    for (int i = 0; i < 26; i++) //Max 개수 체크 
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
