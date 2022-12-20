from collections import deque
import sys
si = sys.stdin.readline
answer = []
N, M, V = map(int, si().split())
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)

# 값 넣기
for i in range(M):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in range(1, N+1):
    graph[i].sort()

def dfs(value):
    visited[value] = 1 # 방문처리
    answer.append(value)

    for i in graph[value]:
        if visited[i] == 0: # 방문 안한 경우에만
            dfs(i)

dfs(V)
print(*answer)
visited = [0] * (N+1)
answer = []


def bfs(value):
    q = deque()
    q.append(value)
    visited[value] = 1 # 방문처리
    while q:
        val = q.popleft()
        answer.append(val)
        for i in graph[val]:
            if visited[i] == 0: # 방문이 아닌 경우에만
                visited[i] = 1 # 방문처리
                q.append(i)
bfs(V)
print(*answer)