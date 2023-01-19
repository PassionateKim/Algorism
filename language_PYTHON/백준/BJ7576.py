# 토마토
# 복습 횟수:3, 00:30:00, 복습 필요
import sys
from collections import deque
si = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, si().split())
tomato_list = []
visited = [[0 for _ in range(M)] for __ in range(N)]
for i in range(N):
    tmp = list(map(int, si().split()))
    tomato_list.append(tmp)

def bfs():
    q = deque()
    for i in range(N):
        for j in range(M):
            if tomato_list[i][j] == 1:
                q.append([i, j, 0]) # 첫날이니까 0으로 한다.
                visited[i][j] = 1 # 방문 처리
            if tomato_list[i][j] == -1:
                visited[i][j] = -1
    
    while q:
        x, y, count = q.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]

            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny] != 0: continue
            if tomato_list[nx][ny] == -1: continue

            q.append([nx, ny, count + 1])
            visited[nx][ny] = visited[x][y] + 1
    return

bfs()
answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0: 
            print(-1)
            exit()
        answer = max(visited[i][j] -1, answer)

print(answer)
