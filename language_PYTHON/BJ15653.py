# 구슬 탈출 4
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# Red Blue 위치 저장하기
for i in range(N):
    for j in range(M):
        if graph[i][j] == "R":
            rx, ry = i, j
        elif graph[i][j] == "B":
            bx, by = i, j

q = deque()
# init
def init():
    q.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = 1 # 방문처리
    return

def bfs():
    init()
    
    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if graph[rx][ry] == 'O':
            print(cnt)
            return

        for i in range(4):
            # Red
            nrx, nry = rx, ry
            while True:
                nrx += dx[i]
                nry += dy[i]

                # 벽에 닿으면 뒤로
                if graph[nrx][nry] == '#':
                    nrx -= dx[i]
                    nry -= dy[i]
                    break
                # 구멍을 통해 빠져 나가면
                if graph[nrx][nry] == 'O':
                    break
            # Blue    
            nbx, nby = bx, by
            while True:
                nbx += dx[i]
                nby += dy[i]

                # 벽에 닿으면 뒤로
                if graph[nbx][nby] == '#':
                    nbx -= dx[i]
                    nby -= dy[i]
                    break
                # 구멍을 통해 빠져 나가면
                if graph[nbx][nby] == 'O':
                    break
            if graph[nbx][nby] == 'O': # 실패 이므로
                continue # 이 방향은 체크할 필요 X
            
            # 위치가 같은 경우 순서 
            if nrx == nbx and nry == nby:
                if abs(nrx-rx) + abs(nry-ry) > abs(nbx-bx) + abs(nby-by):
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if visited[nrx][nry][nbx][nby] == 0: # 방문하지 않았더라면
                q.append((nrx, nry, nbx, nby, cnt+1))
                visited[nrx][nry][nbx][nby] = 1 # 방문처리   
    print(-1)
    return

                    
bfs()
