# 복습 횟수:0, 00:10:00, 복습필요X
import sys
si = sys.stdin.readline

N = int(si())
first_arr = list(map(int, si().split()))
M = int(si())
second_arr = list(map(int, si().split()))

first_set = set(first_arr)

for elem in second_arr:
    if elem in first_set:
        print(1, end=' ')
    else:
        print(0, end=' ')