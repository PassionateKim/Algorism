#DFS 와 BFS
import sys
from collections import deque


def dfs(n):
    print(n)
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)


#node, branch, first node
n,m,v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    

for i in range(1, n+1):
    graph[i].sort()

print(graph)

dfs(v)
