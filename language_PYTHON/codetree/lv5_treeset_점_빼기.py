# 복습 횟수:0, 00:30:00, 복습필요X
from sortedcontainers import SortedSet 
import sys
si = sys.stdin.readline
N, M = map(int, si().split())

s = SortedSet()

for i in range(N):
    x, y = map(int, si().split())
    s.add(tuple([x, y]))

def bisect_right(target):
    start = 0
    end = len(s) - 1
    answer = sys.maxsize
    while (start <= end):
        mid = (start + end) // 2

        if(s[mid][0] >= target):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

for i in range(M):
    input = int(si())
    index = bisect_right(input)

    if(index == sys.maxsize):
        result = [-1, -1]
        print(*result)
    else:
        print(*s[index])
        s.remove(s[index])