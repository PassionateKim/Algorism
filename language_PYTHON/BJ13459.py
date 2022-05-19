# 구슬 탈출
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()

# 빨간색 , 파란색 공의 위치
for x in range(N):
    for y in range(M):
        if graph[x][y] == 'R':
            rx, ry = x, y
        elif graph[x][y] == 'B':
            bx, by = x, y
q.append((rx, ry, bx, by, 0))
visited[rx][ry][bx][by] = 1 # 방문 처리

def bfs():
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break

        if graph[rx][ry] == 'O':
            print(1)
            return

        for i in range(4): # 상하좌우
            nrx, nry = rx, ry # 빨간색 공
            while True: #while문을 통해 쭉
                nrx += dx[i]
                nry += dy[i]

                if graph[nrx][nry] == '#':
                    nrx -= dx[i]
                    nry -= dy[i]
                    break
                if graph[nrx][nry] == 'O':
                    break

            nbx, nby = bx, by # 파란색 공
            while True:
                nbx += dx[i]
                nby += dy[i]

                if graph[nbx][nby] == '#':
                    nbx -= dx[i]
                    nby -= dy[i]
                    break
                if graph[nbx][nby] == 'O':
                    break
            if graph[nbx][nby] == 'O': # 파란공이 들어가면 체크할 필요 없으므로
                continue # 다른 방향 체크
            if nrx == nbx and nry == nby: # 같은 위치일 때
                if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if visited[nrx][nry][nbx][nby] == 0: # 빙문하지 않은 경우
                q.append((nrx, nry, nbx, nby, depth+1))
                visited[nrx][nry][nbx][nby] = 1 # 방문처리
    print(0)


bfs()
