# MooTube (Silver)
# 복습 횟수:1, 01:00:00, 복습필요O
import sys
from collections import deque
N, Q = map(int, sys.stdin.readline().split())
si = sys.stdin.readline

def bfs():
    q = deque()
    visited[v] = 1 # 방문처리
    for nv, nk in graph[v]:
        q.append([nv, nk])
        visited[nv] = 1 # 방문처리
    
    result = 0
    while q:
        ov, ok = q.popleft()
        if ok >= k:
            result += 1

        for nv, nk in graph[ov]:
            if visited[nv] == 1: continue

            q.append([nv, min(nk, ok)])
            visited[nv] = 1 # 방문처리

    return result

graph = [[] for i in range(N+1)]

for i in range(N-1):
    p, q, r = map(int, si().split())
    graph[p].append([q, r])
    graph[q].append([p, r])

for i in range(Q):
    visited = [0 for i in range(N+1)]
    k, v = map(int, si().split())
    print(bfs())