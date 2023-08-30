# 숨바꼭질 3
# 복습 횟수:2, 00:30:00, 복습필요2

from collections import deque
import sys

si = sys.stdin.readline 
N, M = map(int, si().split())

visited = [0 for i in range(100000 + 1)]

def bfs():
    q = deque()
    q.append([N, 0])
    visited[N] = 1  # 방문 처리

    while q:
        x, count = q.popleft()
        if x == M:
            print(count)
            break
        
        if 0 <= 2 * x <= 100000 and visited[2 * x] == 0:
            q.appendleft([2 * x , count])
            visited[2*x] = 1
        if 0 <= x - 1 <= 100000 and visited[x-1] == 0:
            q.append([x - 1, count + 1])
            visited[x-1] = 1
        if 0 <= x + 1 <= 100000 and visited[x+1] == 0:
            q.append([x + 1, count + 1])
            visited[x+1] = 1

    return

bfs()