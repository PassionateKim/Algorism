# 안전 영역
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = -1
# 최댓값
max_val = -1
for row in range(len(graph)):
    if max(graph[row]) >= max_val:
        max_val = max(graph[row])

def bfs(idx):
    cnt = 0
    q = deque()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > idx and visited[i][j] == 0:
                q.append((i,j))
                visited[i][j] = 1 # 방문처리
                cnt += 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if (0 <= nx < N and 0 <= ny < N) and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            if graph[nx][ny] > idx:
                                q.append((nx, ny))
                                # visited[nx][ny] = 1 #방문처리
    return cnt                            

for i in range(1, max_val+1):
    cnt = bfs(i)
    # print(cnt)
    answer = max(cnt, answer)
print(answer)