# 구슬 탙출2 
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R': # 빨간구슬
            rx, ry = i, j
        elif graph[i][j] == 'B': # 파란구슬
            bx, by = i, j
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    count = 0

    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10: # 움직인 횟수 10 초과
                print(-1)
                return
            if graph[rx][ry] == 'O': #현재 빨간 구슬 위치가 구멍이라면
                print(count)
                return
            
            for i in range(4): # 4 방향 탐색
                nrx, nry = rx, ry
                while True: # '#'일 때까지 혹은 구멍일 때까지 움직임
                    nrx = nrx + dx[i]
                    nry = nry + dy[i]
                    if graph[nrx][nry] == '#':# 벽인경우 그대로 한칸 뒤로
                        nrx = nrx - dx[i]
                        nry = nry - dy[i]
                        break
                    if graph[nrx][nry] == 'O': 
                        break
                nbx, nby = bx, by
                while True:
                    nbx = nbx + dx[i]
                    nby = nby + dy[i]
                    if graph[nbx][nby] == '#': #벽인 경우 그대로 한칸 뒤로
                        nbx = nbx - dx[i]
                        nby = nby - dy[i]
                        break
                    if graph[nbx][nby] == "O":
                        break
                
                if graph[nbx][nby] == 'O': # 파란 구슬이 먼저 들어가거나, 동시에 들어가면 안되므로 continue 
                    continue

                if nrx == nbx and nry == nby: #두 구슬 위치 같은 경우
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 뒤에 있던게 더 많이 이동한것이므로
                        nrx = nrx - dx[i]
                        nry = nry - dy[i]
                    else:
                        nbx = nbx - dx[i]
                        nby = nby - dy[i]
                
                if (nrx, nry, nbx, nby) not in visited: # 방문한 적 없다면
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1) # 10회 내에도 구멍에 들어가지 못하는 경웅
bfs(rx, ry, bx, by)

# 동시에 이동하고 순서가 있는데 이를 어떻게 할까?를 고민하다 풀지 못한 문제. 또한 쭉 이동하는데 이를 어떻게 해결할지 답이 안나왔음. 
# 1. Red, Blue 위치 따로 list에 저장안하고, 하는 방법 
# 2. while문을 사용하는 방법
# 3. 동시에 하는 방법




# N, M = map(int, input().split())
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# graph = [list(map(str, input().rstrip())) for _ in range(N)]

# # 빨간공, 파란공 위치
# for i in range(N):
#     for j in range(M):
#         if graph[i][j] == "R":
#             Red_location = (i,j)
#         elif graph[i][j] == "B":
#             Blue_location = (i,j)
#         elif graph[i][j] == "O":
#             Hole_location = (i,j)

# def bfs(cnt):
#     q = deque()
#     q.append((Red_location[0], Red_location[1]), cnt)
#     q.append((Blue_location[0], Blue_location[1]), cnt)

#     while q:
#         x, y, r_cnt = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
                
            

    

# bfs(0)

