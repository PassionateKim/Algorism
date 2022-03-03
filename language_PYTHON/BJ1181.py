#단어 정렬
#알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
#길이가 짧은 것부터
#길이가 같으면 사전 순으로

import sys
N = int(input())

char_array = []
for i in range(N):
    char_array.append(sys.stdin.readline().rstrip())
char_array.sort(key= lambda x : (len(x),x))
print(char_array)