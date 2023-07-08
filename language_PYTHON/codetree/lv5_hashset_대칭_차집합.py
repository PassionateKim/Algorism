# 복습 횟수:0, 00:15:00, 복습필요X
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
A_set = set(list(map(int, si().split())))
B_set = set(list(map(int, si().split())))

A_B_set = A_set - B_set
B_A_set = B_set - A_set

print(len(A_B_set) + len(B_A_set))