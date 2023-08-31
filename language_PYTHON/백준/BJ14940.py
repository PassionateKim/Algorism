# 쉬운 최단 거리
# 복습 횟수:1, 00:30:00, 복습필요X
import sys
from collections import deque

si = sys.stdin.readline 
N, M = map(int, si().split())


graph = []
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            destination = [i, j]

visited = [[0 for i in range(M)] for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q= deque()
    q.append([destination[0], destination[1], 0])

    while q:
        x, y, distance = q.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny] != 0: continue
            if nx == destination[0] and ny == destination[1]: continue
            if graph[nx][ny] == 0: continue

            q.append([nx, ny, distance + 1])
            visited[nx][ny] = distance + 1

    return
bfs()

for i in range(N):
    for j in range(M):
        if i == destination[0] and j == destination[1]: continue
        # 갈 수 있는데 도달하지 못하는 경우
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

for i in visited:
    print(*i)