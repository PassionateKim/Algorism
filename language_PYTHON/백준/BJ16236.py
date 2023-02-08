# 아기 상어
# 복습 횟수:0, 02:00:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline
N = int(si())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
for i in range(N):
    graph.append(list(map(int, si().split())))
answer = 0
shark = 2
point = 2

def bfs(shark, location):
    tmp = []
    q = deque()
    s_x, s_y = location[0], location[1]

    q.append([s_x, s_y, 0])
    visited = [[0 for i in range(N)] for i in range(N)]
    visited[s_x][s_y] = 1 # 방문처리
    while q:
        x, y, cnt = q.popleft()
        
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < N): continue
            if visited[nx][ny] == 1: continue

            if graph[nx][ny] <= shark:
                q.append([nx, ny, cnt+1])
                visited[nx][ny] = 1 #방문처리
                
                if graph[nx][ny] < shark and graph[nx][ny] != 0:
                    tmp.append([nx, ny, cnt+1])
    tmp.sort(key=lambda x: (x[2], x[0], x[1]))
    return tmp 

while True:
    check = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                shark_location = [i, j]
    
    tmp = bfs(shark, shark_location)
    if len(tmp) == 0:
        print(answer)
        break

    target = tmp[0]
    x, y, cnt = target[0], target[1], target[2]
    answer += cnt
    graph[shark_location[0]][shark_location[1]] = 0 # 상어 있던 자리는 0
    graph[x][y] = 9 # 상어 위치 이동

    point = point - 1
    if point == 0:
        shark += 1
        point = shark