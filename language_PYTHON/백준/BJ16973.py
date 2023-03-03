# 직사각형 탈출
# 복습 횟수:0, 01:00:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline
N, M = map(int, si().split())

graph = [list(map(int, si().split())) for _ in range(N)]
h, w, sr, sc, fr, fc = map(int, si().split())
sr, sc, fr, fc = sr - 1, sc - 1, fr - 1, fc - 1
visited = [[0 for __ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

wall = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            wall.append([i, j])

def isEdgeOk(nx, ny, h, w):
    # # 가장 왼쪽 위
    # if not (0 <= nx < N and 0 <= ny < M): return False
    # # 가장 왼쪽 아래
    # if not(0 <= nx+h-1 < N and 0 <= ny < M): return False
    # # 가장 오른쪽 위
    # if not (0 <= nx < N and 0 <= ny+w-1 < M): return False
    # # 가장 오른쪽 아래
    # if not (0 <= nx+h-1 < N and 0 <= ny+w-1 < M): return False

    if 0 <= nx < N and 0 <= ny < M and 0 <= nx+h-1 < N and 0 <= ny+w-1 < M: return True

    return False

def isWallOk(nx, ny, h, w):
    # for x in range(nx, nx + h):
    #     for y in range(ny, ny + w):
    #         if graph[x][y] == 1: return False
    for x, y in wall:
        if nx <= x < nx + h and ny <= y < ny + w:
            return False
    
    return True

def bfs(x, y, cnt):
    q = deque()
    q.append([x, y, cnt])
    visited[x][y] = 1  # 방문처리

    while q:
        x, y, cnt = q.popleft()

        if x == fr and y == fc:
            return cnt
        
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            
            # 꼭지점 체크
            if isEdgeOk(nx, ny, h, w):
                # 직사각형 안에 1이 존재하는지 체크
                if isWallOk(nx, ny, h, w):
                    if visited[nx][ny] == 0: 
                        q.append([nx, ny, cnt + 1])
                        visited[nx][ny] = 1 # 방문처리

    return -1 

print(bfs(sr, sc, 0))