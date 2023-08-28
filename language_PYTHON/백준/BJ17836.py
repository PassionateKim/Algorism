# 공주님을 구해라.
# 복습 횟수:1, 01:00:00, 복습필요3
from collections import deque
import math
import sys
si = sys.stdin.readline 
N, M, T = map(int, si().split())
vistited = [[[0, 0] for i in range(M)] for i in range(N)]
graph = []

for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = 0
def bfs():
    global flag

    q = deque()
    # x, y, count, isGramGet
    q.append([0, 0, 0, 0])
    while q:
        x, y, count, isGramGet = q.popleft()

        if x == N - 1 and y == M - 1:
            if count <= T:
                flag = 1
                return count
            else:
                return

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not ( 0 <= nx < N and 0 <= ny < M): continue

            if isGramGet:
                if vistited[nx][ny][1] == 1: continue

                q.append([nx, ny, count + 1, isGramGet])
                vistited[nx][ny][1] = 1
            else:
                if vistited[nx][ny][0] == 1: continue
                if graph[nx][ny] == 1: continue

                if graph[nx][ny] == 2:
                    q.append([nx, ny, count + 1, 1])

                else:
                    q.append([nx, ny, count + 1, 0])
    
                vistited[nx][ny][0] = 1
                    
    return

candidate = bfs()
if flag:
    print(candidate)
else:
    print("Fail")