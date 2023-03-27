# 치즈
# 복습 횟수:0, 01:00:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline
N, M = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(N)]

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[0 for _ in range(M)] for __ in range(N)]

    q = deque()
    q.append([0, 0])
    visited[0][0] = -1 # 방문 처리

    while q:
        x, y = q.popleft()
        if graph[x][y] == 1: continue # 이미 치즈인 곳이면 탐색할 필요가 없으므로

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny] == -1: continue # 방문 했던 곳이므로
            
            if graph[nx][ny] == 1: # 치즈이면
                visited[nx][ny] += 1 # 터치 횟수 추가
            else:
                visited[nx][ny] = -1 # 치즈가 아니면 방문처리
            q.append([nx, ny]) # q에 추가
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2: # 2번 이상 터치된 경우라면
                graph[i][j] = 0 # 치즈 녹이기
    

while True:
    flag = 1

    # 탈출
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                flag = 0
    if flag:
        break

    bfs()
    answer += 1

print(answer)    