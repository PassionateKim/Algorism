# 숨바꼭질
# 복습 횟수:0, 00:30:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline
N, K = map(int, si().split())
check = set()
def bfs():
    q = deque()
    q.append([N, 0])
    check.add(N)
    while q:
        location, cnt = q.popleft()
        if location == K:
            return cnt
        # 2배
        for i in (location -1 ,location +1, location*2):
            if 0 <= i <= 100000 and not i in check:
                q.append([i, cnt + 1])
                check.add(i)

print(bfs())
