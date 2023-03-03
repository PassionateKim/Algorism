# 쉬운 최단 거리
# 복습 횟수:0, 00:45:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline

N, M = map(int, si().split())

graph = [list(map(int, si().split())) for _ in range(N)]
answer = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():

    q = deque()
    q.append([n, m, 0])
    visited[n][m] = 1 # 방문처리
    answer[n][m] = 0
    
    while q:
        x, y, cnt = q.popleft()
        
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < M): continue
            if visited[nx][ny] == 1: continue
            if graph[nx][ny] == 0: continue

            q.append([nx, ny, cnt + 1])
            answer[nx][ny] = cnt + 1
            visited[nx][ny] = 1 # 방문처리

    return 

# 첫 위치 체크하기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            n, m = i, j

        if graph[i][j] == 0:
            visited[i][j] = 1 # 방문처리 

bfs()
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            answer[i][j] = -1

for i in answer:
    print(*i)

# from collections import deque
# n, m = map(int, input().split())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
    
# visited = [[False for _ in range(m)] for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 2:
#             fx, fy = i, j
#             graph[fx][fy] = 0
#         if graph[i][j] == 0:
#             visited[i][j] = True

# def bfs(x, y, cnt):
#     queue = deque([(x, y, cnt)])
#     visited[x][y] = True

#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]

#     while queue:
#         x, y, cnt = queue.popleft()
#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y

#             if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
#                 if graph[nx][ny] == 1:
#                     queue.append((nx, ny, cnt + 1))
#                     graph[nx][ny] = cnt + 1
#                     visited[nx][ny] = True
#     return

# bfs(fx, fy, 0)

# for i in range(n):
#     for j in range(m):
#         if visited[i][j] == False:
#             graph[i][j] = -1

# for i in range(n):
#     print(*graph[i])