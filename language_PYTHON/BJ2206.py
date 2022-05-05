#벽 부수고 이동하기
import sys
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def BFS(x, y, z):
    
    q = deque()
    q.append([x, y, z])
    visited[x][y][1] = 1 # 벽을 한번 깰 수 있는 상태에서 시작
    while q:
        x, y, z = q.popleft() 

        if x == N-1 and y == M-1:
            return visited[x][y][z]
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M: # 맵 범위 내
                if graph[nx][ny] == 1 and z == 1 and visited[nx][ny][z] == 0: # 벽인데 처음인 경우
                    q.append([nx, ny, 0]) 
                    visited[nx][ny][0] = visited[x][y][z] + 1 # 0으로 꺾어주기
                    
                if graph[nx][ny] == 0 and visited[nx][ny][z] == 0: # 벽이 아닌 경우 방문하지 않았다면
                    q.append([nx, ny, z])
                    visited[nx][ny][z] = visited[x][y][z] + 1 # 방문처리
    return -1

print(BFS(0, 0, 1))
for i in visited:
    print(i)