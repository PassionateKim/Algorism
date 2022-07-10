# 구슬 탙출2 
from collections import deque
import sys
si = sys.stdin.readline

dir = [(-1,0), (1,0), (0,-1), (0,1)]
N, M = map(int, si().split())
graph = []
visited = [[[[0 for _ in range(M)] for __ in range(N)]for ___ in range(M)] for ____ in range(N)] 
# graph 초기화
for i in range(N):
    graph.append(list(map(str, si().strip())))
# 위치 초기화
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

# bfs 
def bfs():
    global rx, ry, bx, by
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = 1 # 방문처리
    
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        # 탈출 조건
        if graph[rx][ry] == 'O':
            print(cnt)
            return
        
        if cnt > 10: # 순서가 이래도 되나??...cnt == 11 이면서 rx ry = 'O' 인 경우는?
            print(-1)
            return
            
        # 상하좌우
        for idx in range(4):
            # Red 공
            nrx, nry = rx + dir[idx][0], ry + dir[idx][1]
            while True:
                # 벽인 경우 뒤로 한칸
                if graph[nrx][nry] == '#':
                    nrx -= dir[idx][0]
                    nry -= dir[idx][1]
                    break
                # O인 경우 
                if graph[nrx][nry] == 'O':
                    break
                
                nrx += dir[idx][0]
                nry += dir[idx][1]

            # Blue 공
            nbx, nby = bx + dir[idx][0], by + dir[idx][1]
            while True:
                # 벽인 경우 뒤로 한칸
                if graph[nbx][nby] == '#':
                    nbx -= dir[idx][0]
                    nby -= dir[idx][1]
                    break
                # 0인 경우
                if graph[nbx][nby] == 'O':
                    break
                
                nbx += dir[idx][0]
                nby += dir[idx][1]

            # Blue공이 구멍에 들어가는 경우는 넣지 않는다.    
            if graph[nbx][nby] =='O': continue
            
            # for 문 라인
            # 만약 위치가 같다면 누가 먼저 왔는지 순서 정하기
            if nrx == nbx and nry == nby: 
                if abs(nrx - rx) + abs(nry - ry) < abs(nbx - bx) + abs(nby - by): # Blue가 더 먼 거리를 이동해왔다면
                    nbx -= dir[idx][0]
                    nby -= dir[idx][1]
                else: # Red가 더 먼거리를 이동해 왔다면
                    nrx -= dir[idx][0]
                    nry -= dir[idx][1]
            
            # visted면 pass
            if visited[nrx][nry][nbx][nby] == 1: continue

            q.append((nrx, nry, nbx, nby, cnt+1)) # q에 넣기
            visited[nrx][nry][nbx][nby] = 1 # 방문처리

    # cnt가 10이하인 것들 중 q를 모두 다돌아도 안되는 경우
    print(-1)
    return

bfs()


# 동시에 이동하고 순서가 있는데 이를 어떻게 할까?를 고민하다 풀지 못한 문제. 또한 쭉 이동하는데 이를 어떻게 해결할지 답이 안나왔음. 
# 1. Red, Blue 위치 따로 list에 저장안하고, 하는 방법 
# 2. while문을 사용하는 방법
# 3. 동시에 하는 방법
# 4. for in range(len(q)): 이후의 count += 1을 통해 순서를 취합한 방법
# 5. 4차원 배열의 쓰임