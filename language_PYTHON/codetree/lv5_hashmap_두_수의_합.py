# 복습 횟수:1, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
num_arr = list(map(int, si().split()))

answer = 0
num_dict = dict()
for num in num_arr:
    if(num not in num_dict.keys()):
        num_dict[num] = 1
    else:
        num_dict[num] += 1

for num in num_arr:
    num_dict[num] -= 1

    diff = M - num
    if diff in num_dict.keys():
        answer += num_dict[diff]

print(answer)