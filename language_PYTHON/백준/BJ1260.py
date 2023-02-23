# DFS와 BFS
# 복습 횟수:3, 00:30:00, 복습필요X
import sys
from collections import deque
si = sys.stdin.readline

N, M, V = map(int, si().split())

graph = [[] for i in range(N+1)] 

for i in range(M):
    x, y = map(int, si().split())
    graph[x].append(y)
    graph[y].append(x)

for val in graph:
    val.sort()

li = []
visited = [0 for i in range(N+1)]
def dfs(start):
    visited[start] = 1 # 방문 처리
    li.append(start)

    for val in graph[start]:
        if visited[val] == 1: continue
        
        dfs(val)

    return

dfs(V)
print(*li)

def bfs(start):
    li = [start]
    visited = [0] * (N+1)
    visited[start] = 1 # 방문처리
    
    q = deque()
    q.append(start)
    while q:
        idx = q.popleft()
        for val in graph[idx]:
            if visited[val] == 1: continue

            q.append(val)
            li.append(val)
            visited[val] = 1 # 방문처리
    
    return li

li = bfs(V)
print(*li)

