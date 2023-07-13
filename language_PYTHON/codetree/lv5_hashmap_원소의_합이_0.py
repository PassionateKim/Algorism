# 2023-07-13
# 복습 횟수:1, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline
N = int(si())
A_list = list(map(int, si().split()))
B_list = list(map(int, si().split()))
C_list = list(map(int, si().split()))
D_list = list(map(int, si().split()))

A_B_dict = dict()

for i in range(len(A_list)):
    for j in range(len(B_list)):
        sumi = A_list[i] + B_list[j]
        if sumi not in A_B_dict.keys():
            A_B_dict[sumi] = 1
        else:
            A_B_dict[sumi] += 1

C_D_dict = dict()


for i in range(len(C_list)):
    for j in range(len(D_list)):
        sumi = C_list[i] + D_list[j]
        if sumi not in C_D_dict.keys():
            C_D_dict[sumi] = 1
        else:
            C_D_dict[sumi] += 1

answer = 0

for key, value in A_B_dict.items():
    diff = 0 - key

    if diff in C_D_dict.keys():
        answer += (value * C_D_dict[diff])

print(answer)