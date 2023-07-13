# 2023-07-13
# 복습 횟수:1, 01:00:00, 복습필요:***
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline 

N, M = map(int, si().split())
s = SortedSet()
answer = sys.maxsize

for i in range(N):
    input = int(si())
    s.add(input)

for target in s:
    # 차이가 m 이상이면서 큰 제일 작은 수의 위치
    bigger_index = s.bisect_left(target + M)
    if (bigger_index != len(s)): # 존재한다면
        answer = min(answer, s[bigger_index] - target)

    # 차이가 m 이상이면서 작은 제일 큰 수의 위치
    less_index = s.bisect_right(target - M) - 1
    if less_index != -1:
        answer = min(answer, target - s[less_index])

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)