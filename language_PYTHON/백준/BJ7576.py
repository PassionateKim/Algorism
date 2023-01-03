# 토마토
import sys
from collections import deque
si = sys.stdin.readline

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []

M, N = map(int, si().split())

for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

answer = 0
riped_tomato = 0
no_tomato = 0
def bfs():
    global riped_tomato
    global no_tomato
    q = deque()
    tmp = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                riped_tomato = riped_tomato + 1
                q.append((i, j, 0))

            if graph[i][j] == -1:
                no_tomato = no_tomato + 1
    # 첫번째 경우                
    if no_tomato + riped_tomato == N * M :
        print(0)
        exit()

    while q:
        x, y, count = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M): continue # 범위 넘었을 시 continue
            if graph[nx][ny] != 0: continue

            q.append((nx, ny, count+1))
            graph[nx][ny] = count + 1
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                print(-1)
                exit()
    return        

bfs()

for i in range(N):
    answer = max(answer, max(graph[i]))

print(answer)