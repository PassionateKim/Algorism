# 복습 횟수:0, 00:15:00,  복습필요X
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
s = SortedSet()

for i in range(N):
    x, y = map(int, si().split())
    s.add(tuple([x, y]))

    
for j in range(M):
    query_x, query_y = map(int, si().split())
    tmp = tuple([query_x, query_y])
    