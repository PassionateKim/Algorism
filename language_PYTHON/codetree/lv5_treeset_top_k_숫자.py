# 복습 횟수:0, 00:10:00, 복습필요:X
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline

N, M = map(int, si().split())
arr_list = list(map(int, si().split()))
s = SortedSet()

for arr in arr_list:
    s.add(arr)

for i in range(M):
    print(s[-1-i], end=' ')
