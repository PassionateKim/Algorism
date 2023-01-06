# 미로탐색
import sys
from collections import deque
si = sys.stdin.readline
N, M = map(int, si().split())
graph = []
dx = [-1, 1, 0, 0] # 상하
dy = [0, 0, -1, 1] # 좌우

visited = [[0 for i in range(M)] for i in range(N)]

# graph 생성하기
for i in range(N):
    tmp = list(map(int, si().rstrip()))
    graph.append(tmp)


def bfs():
    q = deque()

    q.append([0,0,1])
    visited[0][0] = 1 # 방문처리

    while q:
        x, y, count = q.popleft()
        # 탈출 조건
        if (x == N-1 and y == M-1):
            print(count)
            return

        # 상하좌우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny] != 0: continue
            if graph[nx][ny] == 0: continue
            
            q.append([nx, ny, count + 1])
            visited[nx][ny] = 1 # 방문처리

bfs()