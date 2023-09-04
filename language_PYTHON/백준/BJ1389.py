# 복습 횟수:0, 00:30:00, 복습필요X
from collections import deque
import sys
si = sys.stdin.readline 
N, M = map(int, si().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    x, y = map(int, si().split())
    graph[x].append(y)
    graph[y].append(x)

answer = []

def bfs(start, target):

    q = deque()
    q.append([start, 0])
    visited[start] = 1  #방문처리
    
    while q:
        start, index = q.popleft()
        if start == target:
            return index

        for end in graph[start]:
            if visited[end] == 0:

                q.append([end, index + 1])
                visited[end] = 1 # 방문처리

    return

for i in range(1, N + 1): # 수
    candidate = 0
    for j in range(1, N + 1):
        if i == j: continue

        visited = [0 for i in range(N+1)]
        candidate += bfs(i, j)

    answer.append(candidate)

print(answer.index(min(answer)) + 1)