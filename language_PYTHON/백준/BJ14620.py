# 꽃길
# 복습 횟수:0, 01:00:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline
N = int(si())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)
answer = sys.maxsize

# 완전 탐색
for i in range(1, N-1):
    for j in range(1, N-1):
        visited = [[0 for i in range(N)] for i in range(N)]
        # 첫번째 꽃
        visited[i][j] = 1 # 방문처리
        for idx in range(4):
            ni, nj = i + dx[idx], j + dy[idx]
            visited[ni][nj] = 1 # 방문처리
        
        # 두번째 꽃
        for k in range(1, N-1):
            for l in range(1, N-1):
                q = deque()
                q.append([k, l])
                for idx in range(4):
                    nk, nl = k + dx[idx], l + dy[idx]
                    q.append([nk, nl])
                
                tmp = 0
                for x, y in q:
                    if visited[x][y] == 1:
                        tmp += 1
                if tmp > 0: continue
                
                for x, y in q:
                    visited[x][y] = 1 

                # 세번째 꽃
                for x in range(1, N-1):
                    for y in range(1, N-1):
                        q2 = deque()
                        q2.append([x, y])
                        for idx in range(4):
                            nx, ny = x + dx[idx], y + dy[idx]
                            q2.append([nx, ny])
                        
                        tmp = 0
                        for x, y in q2:
                            if visited[x][y] == 1:
                                tmp += 1
                        if tmp > 0: continue
                        
                        for x, y in q2:
                            visited[x][y] = 1 # 방문처리

                        # 여기까지 코드가 도착하는 경우 겹치지 않는 것임
                        sumi = 0
                        for xx in range(N):
                            for yy in range(N):
                                if visited[xx][yy] == 1:
                                    sumi += graph[xx][yy]
                        
                        answer = min(answer, sumi)

                        for x, y in q2:
                            visited[x][y] = 0 # 원상복구
                # 원상복구
                for x, y in q:
                    visited[x][y] = 0 
print(answer)