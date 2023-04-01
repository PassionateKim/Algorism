# 빙산
# 복습 횟수:0, 01:00:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline

N, M = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = -1 # 방문처리

    while q:
        x, y = q.popleft()
        if graph[x][y] > 0: continue

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny] == -1: continue

            if graph[nx][ny] != 0:
                visited[nx][ny] += 1
            else:
                visited[nx][ny] = -1 
            
            q.append([nx, ny])
    
    return

def bfs2(i, j, count):
    q = deque()
    q.append([i, j])
    visited2[i][j] = count
    
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited2[nx][ny] == count: continue

            if graph[nx][ny] != 0:
                q.append([nx, ny])
                visited2[nx][ny] = count
    
    return True

answer = 0

while True: 
    flag = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                flag = 0
                break
        if flag == 0:
            break
    
    # 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.
    if flag:
        print(0)
        break
    
    # 두 덩어리 이상으로 분리되면 출력한다.
    count = 1
    visited2 = [[0 for _ in range(M)] for __ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0: continue
            if visited2[i][j] != 0: continue

            if bfs2(i, j, count):
                count += 1
    if count > 2:
        print(answer)
        break
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] == -1: continue
            if graph[i][j] != 0: continue

            bfs(i, j)
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] > 0:
                val = graph[i][j] - visited[i][j]
                if val < 0:
                    val = 0
                
                graph[i][j] = val
    
    answer += 1