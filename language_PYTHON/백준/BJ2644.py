# 촌수 계산
# 복습 횟수:0, 00:30:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline
N = int(si())
a, b = map(int, si().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

M = int(si())
for i in range(M):
    x, y = map(int, si().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(a, b):
    q = deque()
    q.append([a, 0])
    visited[a] = 1 # 방문처리
    while q:
        location, cnt = q.popleft()
        if location == b:
            return cnt
        
        for val in graph[location]:
            if visited[val] == 0:
                q.append([val, cnt + 1])
                visited[val] = 1 # 방문처리

    return -1

print(bfs(a, b))