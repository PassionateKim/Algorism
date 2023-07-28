# MooTube (Silver)
# 복습 횟수:2, 01:00:00, 복습필요3
import sys
from collections import deque
si = sys.stdin.readline 

N, Q = map(int, si().split())

graph = [[] for i in range(N+1)]

for i in range(N-1):
    x, y, usado = map(int, si().split())
    graph[x].append([y, usado])
    graph[y].append([x, usado])


def bfs(k, start):
    visited = [0 for i in range(N+1)]
    visited[start] = 1 # 방문 처리
    q = deque()
    q.append([start, 1e11])
    answer = 0
    while q:
        start, current_usado = q.popleft()
        if current_usado >= k:
            answer += 1

        for target, target_usado in graph[start]:
            if visited[target] == 0:
                q.append([target, min(target_usado, current_usado)])
                visited[target] = 1 # 방문처리

    return answer - 1

for i in range(Q):
    k, v = map(int, si().split())
    print(bfs(k, v))