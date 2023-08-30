# 직사각형 탈출
# 복습 횟수:1, 01:00:00, 복습필요2
from collections import deque
import sys
si = sys.stdin.readline 

N, M = map(int, si().split())
graph = []

for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

H, W, Sr, Sc, Fr, Fc = map(int ,si().split())
# index 1 -> 0 

Sr = Sr - 1
Sc = Sc - 1
Fr = Fr - 1
Fc = Fc - 1

visited = [[0 for i in range(M)] for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


wall_list = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            wall_list.append([i, j])

def isEdgeOk(nx ,ny):
    if not (0 <= nx < N and 0 <= ny < M): return False
    if not (0 <= nx + H - 1 < N and 0 <= ny + W - 1 < M): return False

    return True

def isWallOk(nx, ny):
    for wall_x, wall_y in wall_list:
        if (nx <= wall_x < nx + H) and (ny <= wall_y < ny + W): return False

    return True

def bfs():
    q = deque()
    # 왼쪽 상부 꼭지점 x, y 좌표
    q.append([Sr, Sc, 0])
    visited[Sr][Sc] = 1 # 방문 처리

    while q:
        x, y, count = q.popleft()
        
        if x == Fr and y == Fc:
            print(count)
            return

        for idx in range(4):
            nx,  ny = x + dx[idx], y + dy[idx]

            if isEdgeOk(nx, ny) and isWallOk(nx, ny):
                if visited[nx][ny] == 1: continue

                q.append([nx, ny, count + 1])
                visited[nx][ny] = 1 # 방문 처리

    print(-1)
    return

bfs()