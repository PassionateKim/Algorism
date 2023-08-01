# 토마토
# 복습 횟수:4, 00:30:00, 복습 필요X
from collections import deque
import sys
si = sys.stdin.readline 
M, N = map(int, si().split())
graph = []

for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():

    visited = [[0 for i in range(M)] for i in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1: 
                q.append([i, j, 1])
                visited[i][j] = 1 # 방문처리


    while q:
        x, y, day = q.popleft()
        
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny] != 0: continue
            if graph[nx][ny] == -1: continue

            q.append([nx, ny, day + 1])
            visited[nx][ny] = day + 1

    flag = False
    answer = 0
    for i in range(N):
        for j in range(M):
            answer = max(answer, visited[i][j])
            if visited[i][j] == 0 and graph[i][j] != -1:
                flag = True

    if flag:
        return -1
    else:
        return answer - 1 

print(bfs())