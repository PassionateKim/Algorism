# 치즈
# 복습 횟수:1, 00:45:00, 복습필요X
import sys
from collections import deque
si = sys.stdin.readline 
N, M = map(int, si().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []

for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = -1 # 방문처리

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M): continue

            if graph[nx][ny] == 1: # cheese 라면 
                visited[nx][ny] += 1 # +=1 이따 2번이상인 것을 체크해야하므로
                continue

            if visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = -1 # 방문처리
    
    return

answer = 0
while True:
    flag = True
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                flag = False
    
    if flag:
        print(answer)
        break

    visited = [[0 for i in range(M)] for i in range(N)]

    bfs(0,0)

    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                graph[i][j] = 0 # 치즈가 녹는다.    
        
    
    answer += 1