# 연결 요소의 개수

import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int, si().split())
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)

# 1. 그래프 간선 세팅하기
for i in range(M):
    x, y = map(int, si().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

# 2. DFS로 탐색하기 with cnt
def dfs(param):
    visited[param] = 1 # 방문 처리
    
    for i in graph[param]:    
        if visited[i] == 0: #방문하지 않은 경우에만
            dfs(i)
    return

cnt = 0
for i in range(1, len(graph)):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
    
print(cnt)