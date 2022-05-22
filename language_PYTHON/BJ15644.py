# 구슬 탈출 3
from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(input().rstrip()) for i in range(N)]
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#Red, Blue 위치
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j
q = deque()
q.append((rx, ry, bx, by, 0, ''))
visited[rx][ry][bx][by] = 1 # 방문 처리


def bfs():
    while q:
        rx, ry, bx, by, cnt, way_list = q.popleft()
        
        if cnt > 10:
            print(-1)
            return

        if graph[rx][ry] == 'O':
            print(cnt)
            if cnt != 0:
                print(way_list)
            return

        for i in range(4): # 상하좌우
            nrx, nry = rx, ry # RED
            while True: # 특정방향으로 계속 이동
                nrx += dx[i]
                nry += dy[i]

                if graph[nrx][nry] == '#': # #을 만나면 한칸 뒤로
                    nrx -= dx[i]
                    nry -= dy[i]
                    break
                if graph[nrx][nry] == 'O': # O를 만나면 일단 break
                    break
            nbx, nby = bx, by # BLUE
            while True:
                nbx += dx[i]
                nby += dy[i]

                if graph[nbx][nby] == '#':
                    nbx -= dx[i]
                    nby -= dy[i]
                    break
                if graph[nbx][nby] == 'O':
                    break
            if graph[nbx][nby] == 'O': #BLUE공이 O로 들어가는 경우 
                continue  #더이상 체크할 필요가 없으므로
            
            if nrx == nbx and nry == nby: # 같은 위치에 도달하는 경우
                if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            if visited[nrx][nry][nbx][nby] == 0: # 방문하지 않았던 경우만
                if i == 0: # 상
                    r_way_list = way_list + 'U'
                    q.append((nrx, nry, nbx, nby, cnt+1, r_way_list))
                elif i == 1: # 하
                    r_way_list = way_list + 'D'
                    q.append((nrx, nry, nbx, nby, cnt+1, r_way_list))
                elif i == 2: # 좌
                    r_way_list = way_list + 'L'
                    q.append((nrx, nry, nbx, nby, cnt+1, r_way_list))
                elif i == 3: # 우
                    r_way_list = way_list + 'R'
                    q.append((nrx, nry, nbx, nby, cnt+1, r_way_list))
                visited[nrx][nry][nbx][nby] = 1 # 방문처리    
    # 구슬을 뺄 수 없는 경우
    print(-1)


bfs()
