# 구슬탈출
import sys
from collections import deque
si = sys.stdin.readline

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M = map(int, si().split())
visited = [[[[0 for i in range(M)] for i in range(N)] for i in range(M)] for i in range(N)]

graph = []
for i in range(N):
    tmp = list(map(str, si().rstrip()))
    graph.append(tmp)

# 빨간공, 파란공 위치 찾기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            rx, ry = i, j
        
        elif graph[i][j] == 'B':
            bx, by = i, j

q = deque()
q.append((rx, ry, bx, by, 0))

visited[rx][ry][bx][by] = 1 # 방문처리

def bfs():
    while q:
        rx, ry, bx, by, count = q.popleft()
        
        if (count > 10):
            break 
    
        if graph[rx][ry] == 'O':
            print(1)
            return
        
        for i in range(4):
            # RED
            nrx, nry = rx, ry
            while True:
                nrx += dx[i]
                nry += dy[i]

                # 탈출조건1 - 벽
                if graph[nrx][nry] == '#':
                    nrx -= dx[i]
                    nry -= dy[i]
                    break

                # 탈출조건2 - 구멍
                if graph[nrx][nry] == 'O':
                    break
            
            # BLUE
            nbx, nby = bx, by
            while True:
                nbx += dx[i]
                nby += dy[i]

                # 탈출조건1 - 벽
                if graph[nbx][nby] == '#':
                    nbx -= dx[i]
                    nby -= dy[i]
                    break

                # 탈출조건2 - 구멍
                if graph[nbx][nby] == 'O':
                    break
            
            # Blue가 구멍에 들어가면 탐색할 가치가 없으므로
            if graph[nbx][nby] == 'O': continue

            # BLUE와 RED가 같은 위치라면 더 멀리서 온 것을 뒤로 빼야한다.
            if (nrx == nbx and nry == nby):
                if( abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by) ):
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            if visited[nrx][nry][nbx][nby] == 0:
                q.append((nrx, nry, nbx, nby, count+1))
                visited[nrx][nry][nbx][nby] = 1 # 방문처리    
    print(0)

bfs()