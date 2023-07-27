# 빙산
# 복습 횟수:1, 00:30:00, 복습필요X
import sys
from collections import deque
si = sys.stdin.readline 

N, M = map(int, si().split())

graph = []

for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

answer = 0
dx = [-1, 1, 0, 0]
dy =[0, 0, -1, 1]
def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = cnt

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i],  y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M): continue

            if visited[nx][ny] == 0:
                if graph[nx][ny] != 0:
                    q.append([nx, ny])
                    visited[nx][ny] = cnt
    return
while True:
    # 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면
    flag = True
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                flag = False
    
    if flag:
        print(0)
        break

    cnt = 1
    visited = [[0 for i in range(M)] for i in range(N)]
   
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and graph[i][j] != 0:
                bfs(i, j)
                cnt += 1

    # 두 개이상으로 분리되었다면  
    if cnt >= 3:
        print(answer)
        break

    # 빙산 녹이기
    tmp_list = [[0 for i in range(M)] for i in range(N)]

    for x in range(N):
        for y in range(M):
            if graph[x][y] != 0: # 빙산일 때
                tmp = 0
                for idx in range(4):
                    nx, ny = x + dx[idx], y + dy[idx]
                    if not (0 <= nx < N and 0 <= ny < M): continue
                    if graph[nx][ny] == 0:
                        tmp += 1
                
                tmp_list[x][y] = tmp
    # 빙산 녹이기
    for x in range(N):
        for y in range(M):
            if graph[x][y] != 0:
                graph[x][y] = graph[x][y] - tmp_list[x][y]

                if graph[x][y] < 0:
                    graph[x][y] = 0
    
    answer += 1