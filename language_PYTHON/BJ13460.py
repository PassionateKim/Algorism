# 구슬 탙출2 
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(n)]
visited =[[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def init():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "R":
                rx, ry = i, j
            if graph[i][j] == "B":
                bx, by = i, j
    
    q.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = True # 방문처리

def bfs():
    init()

    while q:
        rx, ry, bx, by, depth = q.popleft() #FIFO

        if depth > 10:
            break
        if graph[rx][ry] == 'O':
            print(depth)
            return
        
        for i in range(4): # 상하좌우 체크하기
            # 빨간공
            nrx, nry = rx, ry 
            while True:
                nrx = nrx + dx[i]
                nry = nry + dy[i]

                if graph[nrx][nry] == '#':
                    nrx = nrx - dx[i] # 원위치
                    nry = nry - dy[i] # 원위치
                    break
                if graph[nrx][nry] == 'O': #구멍인 경우
                    break
            # 파란공
            nbx, nby = bx, by 
            while True:
                nbx = nbx + dx[i]
                nby = nby + dy[i]

                if graph[nbx][nby] == '#':
                    nbx = nbx - dx[i] # 원위치
                    nby = nby - dy[i] # 원위치
                    break
                if graph[nbx][nby] == 'O': #구멍인 경우
                    break
            if graph[nbx][nby] == 'O': # 구멍인 경우체크할 필요 없으므로
                continue    # 다음 반복으로 이동한다.ㄷ
            if nrx == nbx and nry == nby: # 위치 같은 경우일 때
                if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더 이동한것이 더 이전 것이므로
                    nrx = nrx - dx[i] # 한칸 뒤로 이동
                    nry = nry - dy[i] # 한칸 뒤로 이동
                else: # 같은 위치일 순 없으므로 '=' 는 없는 조건
                    nbx = nbx - dx[i]
                    nby = nby - dy[i]
            
            if visited[nrx][nry][nbx][nby] == False:
                q.append((nrx, nry, nbx, nby, depth+1))
                visited[nrx][nry][nbx][nby] = True
    print(-1)
bfs()
            

            
            
            
            

        
                                
                














# n, m = map(int, input().split())
# graph = [list(input().rstrip()) for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 'R': # 빨간구슬
#             rx, ry = i, j
#         elif graph[i][j] == 'B': # 파란구슬
#             bx, by = i, j
# # 상하좌우
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(rx, ry, bx, by):
#     q = deque()
#     q.append((rx, ry, bx, by))
#     visited = []
#     visited.append((rx, ry, bx, by))
#     count = 0

#     while q:
#         for _ in range(len(q)):
#             rx, ry, bx, by = q.popleft()
#             if count > 10: # 움직인 횟수 10 초과
#                 print(-1)
#                 return
#             if graph[rx][ry] == 'O': #현재 빨간 구슬 위치가 구멍이라면
#                 print(count)
#                 return
            
#             for i in range(4): # 4 방향 탐색
#                 nrx, nry = rx, ry
#                 while True: # '#'일 때까지 혹은 구멍일 때까지 움직임
#                     nrx = nrx + dx[i]
#                     nry = nry + dy[i]
#                     if graph[nrx][nry] == '#':# 벽인경우 그대로 한칸 뒤로
#                         nrx = nrx - dx[i]
#                         nry = nry - dy[i]
#                         break
#                     if graph[nrx][nry] == 'O': 
#                         break
#                 nbx, nby = bx, by
#                 while True:
#                     nbx = nbx + dx[i]
#                     nby = nby + dy[i]
#                     if graph[nbx][nby] == '#': #벽인 경우 그대로 한칸 뒤로
#                         nbx = nbx - dx[i]
#                         nby = nby - dy[i]
#                         break
#                     if graph[nbx][nby] == "O":
#                         break
                
#                 if graph[nbx][nby] == 'O': # 파란 구슬이 먼저 들어가거나, 동시에 들어가면 안되므로 continue 
#                     continue

#                 if nrx == nbx and nry == nby: #두 구슬 위치 같은 경우
#                     if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 뒤에 있던게 더 많이 이동한것이므로
#                         nrx = nrx - dx[i]
#                         nry = nry - dy[i]
#                     else:
#                         nbx = nbx - dx[i]
#                         nby = nby - dy[i]
                
#                 if (nrx, nry, nbx, nby) not in visited: # 방문한 적 없다면
#                     q.append((nrx, nry, nbx, nby))
#                     visited.append((nrx, nry, nbx, nby))
#         count += 1
#     print(-1) # 10회 내에도 구멍에 들어가지 못하는 경웅
# bfs(rx, ry, bx, by)

# 동시에 이동하고 순서가 있는데 이를 어떻게 할까?를 고민하다 풀지 못한 문제. 또한 쭉 이동하는데 이를 어떻게 해결할지 답이 안나왔음. 
# 1. Red, Blue 위치 따로 list에 저장안하고, 하는 방법 
# 2. while문을 사용하는 방법
# 3. 동시에 하는 방법
# 4. for in range(len(q)): 이후의 count += 1을 통해 순서를 취합한 방법
# 5. 4차원 배열의 쓰임