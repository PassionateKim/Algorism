# 치즈
# 복습 횟수:1, 01:00:00, 복습필요O
from collections import deque
import sys
si = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M = map(int, si().split())

graph = [list(map(int, si().split())) for _ in range(N)]

time = 0
answer = []
def find_air():
    cnt = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1 # 방문처리

    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if not (0 <= nx < N and 0 <= ny < M): continue

            if visited[nx][ny]: continue
            
            if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                q.append([nx, ny])
            
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 산화
                cnt += 1

            visited[nx][ny] = 1 # 방문처리
    
    answer.append(cnt)

    return cnt

while True:
    cnt = find_air()
    
    if cnt == 0:
        break

    time += 1

print(time)
print(answer[-2])