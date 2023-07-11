# 복습 횟수:0, 00:15:00, 복습필요X
from sortedcontainers import SortedSet

import sys
si = sys.stdin.readline 

N, M = map(int, si().split())
s = SortedSet()

for i in range(1, M+1):
    s.add(i)

delete_list = list(map(int, si().split()))
for delete in delete_list:
    s.remove(delete)
    print(s[-1])