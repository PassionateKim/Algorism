# 숨바꼭질
# 복습 횟수:1, 00:30:00, 복습필요2
import sys
from collections import deque

si = sys.stdin.readline 
N, K = map(int, si().split())
def bfs(start):
    visited = [0 for i in range(100001)]
    visited[start] = 1 # 방문처리
    q = deque()
    q.append([start, 0])

    while q:
        start, time = q.popleft()
        if start == K:
            print(time)
            break
        
        if 0 <= start - 1 <= 100000:
            if visited[start - 1] == 0:
                q.append([start -1, time + 1])
                visited[start - 1] = 1 # 방문 처리
        
        if 0 <= start + 1 <= 100000:
            if visited[start + 1] == 0:
                q.append([start + 1, time + 1]) 
                visited[start + 1] = 1 # 방문처리

        if 0 <= start * 2 <= 100000:
            if visited[start * 2] == 0:
                q.append([start*2, time + 1])
                visited[start * 2] = 1 # 방문처리

    return

bfs(N)