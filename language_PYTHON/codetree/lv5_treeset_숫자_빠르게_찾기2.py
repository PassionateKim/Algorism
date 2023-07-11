# 복습 횟수:0, 00:10:00, 복습필요X
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline

N, M = map(int, si().split())
arr_list = list(map(int, si().split()))

s = SortedSet()
for arr in arr_list:
    s.add(arr)

for i in range(M):
    val = int(si())
    index = s.bisect_left(val) 

    if(index == len(arr_list)):
        print(-1)
    else:
        print(s[index])