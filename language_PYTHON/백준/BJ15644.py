# 구슬 탈출 3
from collections import deque
import sys
si = sys.stdin.readline

graph = []
dir = [(-1,0), (1,0), (0,-1), (0,1)]
N, M = map(int, si().split())
visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

for i in range(N):
    graph.append(list(map(str, si().strip())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

q = deque()
q.append([rx, ry, bx, by, 0, ""])
visited[rx][ry][bx][by] = 1 # 방문처리
flag = 0
while q:
    rx, ry, bx, by, cnt, order = q.popleft()

    if cnt > 10:
        print(-1)
        flag = 1
        break
        
    # 탈출 조건
    if graph[rx][ry] == 'O':
        print(cnt)
        print(order)
        flag = 1
        break

    for i in range(4):
        # Red 공
        nrx, nry = rx , ry 
        while True:
            # 한칸 방향으로 이동
            nrx += dir[i][0]
            nry += dir[i][1]

            # 벽을 만나면 한칸 뒤로
            if graph[nrx][nry] == '#':
                nrx -= dir[i][0]
                nry -= dir[i][1]
                break
            
            # 구멍을 만나면 break
            if graph[nrx][nry] == 'O':
                break
        # Blue 공
        nbx, nby = bx, by
        while True:
            # 한칸 방향으로 이동
            nbx += dir[i][0]
            nby += dir[i][1]

            # 벽을 만나면 한칸 뒤로
            if graph[nbx][nby] == '#':
                nbx -= dir[i][0]
                nby -= dir[i][1]
                break

            # 구멍을 만나면 break
            if graph[nbx][nby] == 'O':
                break

        if graph[nbx][nby] == 'O': continue # 탐색필요X
        
        # 같으면 순서 비교
        if nrx == nbx and nry == nby:
            if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                nrx -= dir[i][0]
                nry -= dir[i][1]
            else:
                nbx -= dir[i][0]
                nby -= dir[i][1]
        
        if visited[nrx][nry][nbx][nby] == 0: # 방문한 적이 없다면
            visited[nrx][nry][nbx][nby] = 1 # 방문처리
            if i == 0: # 상
                q.append([nrx, nry, nbx, nby, cnt+1, order+'U'])
            elif i == 1: # 하
                q.append([nrx, nry, nbx, nby, cnt+1, order+'D'])
            elif i == 2: # 좌
                q.append([nrx, nry, nbx, nby, cnt+1, order+'L'])
            else: # 우
                q.append([nrx, nry, nbx, nby, cnt+1, order+'R'])

if flag == 0:
    print(-1)
