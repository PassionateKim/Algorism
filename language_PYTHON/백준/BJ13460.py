from collections import deque

import sys
si = sys.stdin.readline 

N, M = map(int, si().split())

graph = []

for i in range(N):
    input_ = list(map(str, si().rstrip()))
    graph.append(input_)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            rx, ry = i, j
        
        if graph[i][j] == 'B':
            bx, by = i, j
        
        if graph[i][j] == 'O':
            hx, hy = i, j


def bfs():
    global rx, ry, bx, by, hx, hy

    q= deque()
    q.append([0, rx, ry, bx, by])

    visited = [[[[0 for i in range(M)] for i in range(N)] for i in range(M)] for i in range(N)]
    while q:
        count, rx, ry, bx, by = q.popleft()
        visited[rx][ry][bx][by] = 1 # 방문처리

        if count >= 10:
            print(-1)
            return
        
        # 상하좌우
        for idx in range(4):
            hole_red = 0
            hole_blue = 0
            
            nrx, nry = rx, ry
            while True:
                nrx, nry = nrx + dx[idx], nry + dy[idx]
                # 범위를 벗어나거나, 벽에 부딪힌 경우 break 
                if not (0 <= nrx < N and 0 <= nry < M) or graph[nrx][nry] == '#':
                    nrx, nry = nrx - dx[idx], nry - dy[idx] # 다시 원위치 
                    break

                if nrx == hx and nry == hy:
                    hole_red = 1
                    break

            nbx, nby = bx, by
            while True:
                nbx, nby = nbx + dx[idx], nby + dy[idx]

                if not (0 <= nbx < N and 0 <= nby < M) or graph[nbx][nby] == '#':
                    nbx, nby = nbx - dx[idx], nby - dy[idx]
                    break
                
                # blue 가 들어가면 그냥 종료
                if nbx == hx and nby == hy:
                    hole_blue = 1
                    break

            if hole_blue:
                continue
            
            if nrx == nbx and nry == nby:
                if( abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by)):
                    nrx, nry = nrx - dx[idx], nry - dy[idx]
                else:
                    nbx, nby = nbx - dx[idx], nby - dy[idx]
            
            if hole_red:
                print(count + 1)
                return
            
            if visited[nrx][nry][nbx][nby] == 0:
                q.append([count + 1, nrx, nry, nbx, nby])

    print(-1)
    return

bfs()


# 아래에서 count + 1 에서 return 이므로 
# 탈출 조건은 count >= 10으로 해야한다. 