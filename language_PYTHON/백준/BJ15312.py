# 복습 횟수:0, 00:30:00, 복습필요:***
import sys
si = sys.stdin.readline 

A = list(map(str, si().rstrip()))
B = list(map(str, si().rstrip()))
alphabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
answer = []
for word_a, word_b in zip(A, B):
    
    a_index = (ord(word_a) - 65)
    b_index = (ord(word_b) - 65)

    a_alphabet = alphabet[a_index]
    b_alphabet = alphabet[b_index]
    answer.append(a_alphabet)
    answer.append(b_alphabet)

while True:
    if len(answer) == 2:
        print(str(answer[0]) + str(answer[1]))
        break

    tmp = []
    for i in range(len(answer) - 1):
        val = answer[i] + answer[i+1]
        if val >= 10:
            val = val - 10
        tmp.append(val)
    
    answer = tmp[:]