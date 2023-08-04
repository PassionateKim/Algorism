# 이분 그래프
# 복습 횟수:2, 00:30:00, 복습필요X

import sys
from collections import deque
si = sys.stdin.readline 
K = int(si())
def bfs(k, graph):
    global flag

    q = deque()
    q.append(k)
    visited[k] = 1
    while q:
        start = q.popleft()
        for end in graph[start]:
            if visited[end] == 0:
                q.append(end)
                visited[end] = -visited[start]
            if visited[end] != 0:
                # check
                if visited[start] == visited[end]:
                    flag = False
                    return 

for i in range(K):
    V, E = map(int, si().split())
    graph = [[] for i in range(V+1)]
    # graph 초기화
    for j in range(E):
        x, y = map(int, si().split())
        graph[x].append(y)
        graph[y].append(x)
        
    visited = [0 for i in range(V+1)]
    flag = True
    for k in range(1, V+1):
        if visited[k] == 0:
            bfs(k, graph)

    if flag:
        print("YES")
    else:
        print("NO")