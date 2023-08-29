# 트리의 부모 찾기
# 복습 횟수:2, 00:30:00, 복습필요X
from collections import deque
import sys

si = sys.stdin.readline 
N = int(si())

graph = [[] for i in range(N + 1)]
parent = [0 for i in range(N + 1)]

for i in range(N - 1):
    x, y = map(int, si().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs():
    q = deque()
    q.append(1)
    parent[1] = 1

    while q:
        start_index = q.popleft()
        for end_index in graph[start_index]:
            
            if parent[end_index] == 0:
                parent[end_index] = start_index
                q.append(end_index)

    return

bfs()
for i in range(2, len(parent)):
    print(parent[i])
    