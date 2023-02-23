# 공주님을 구해라.
# 복습 횟수:0, 01:00:00, 복습필요O
import sys
from collections import deque   
si = sys.stdin.readline

N, M, K = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs( time):
    q = deque()
    visited = [[[0, 0] for i in range(M)] for j in range(N)]

    q.append([0, 0, 0, 0])
    visited[0][0][0] = 1 # 방문처리
    while q:
        x, y, knife, time = q.popleft()
        if x == N-1 and y == M-1:
            if time <= K:
                print(time)
            else:
                print('Fail')
            return
        
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0 <= nx < N and 0 <= ny < M): continue
            
            if knife == 1:
                if visited[nx][ny][1]: continue

                q.append([nx, ny, 1, time + 1])
                visited[nx][ny][1] = 1 # 방문처리
            else:
                if visited[nx][ny][0]: continue
                if graph[nx][ny] == 1: continue

                if graph[nx][ny] == 2:
                    q.append([nx, ny, 1, time + 1])
                else:
                    q.append([nx, ny, 0, time + 1])

                visited[nx][ny][0] = 1 # 방문처리
    
    print('Fail')
bfs(0)