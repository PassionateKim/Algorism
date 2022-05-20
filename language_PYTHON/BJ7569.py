#토마토 3D
import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
# 상하좌우위아래
dx = [-1,1,0,0,-N,N]
dy = [0,0,-1,1,0,0]
graph = []
for i in range(N*H):
    graph.append(list(map(int, input().split())))
ripen_tomato_cnt = 0
no_tomato_cnt = 0
# 초기화
q = deque()
for i in range(N*H):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i,j,0))
            ripen_tomato_cnt += 1
        elif graph[i][j] == -1:
            no_tomato_cnt += 1
 
def bfs():
    global ripen_tomato_cnt
    global no_tomato_cnt
    # 저장될 때부터 모든 토마토가 익어있는 상태면 0 출력
    if ripen_tomato_cnt == M*N*H - no_tomato_cnt: 
        print(0)
        return

    while q:
        r_x, r_y, day = q.popleft()
        
        for i in range(6):
            nx = r_x + dx[i] 
            ny = r_y + dy[i]
            
            if 0 <= nx < N*H and 0 <= ny < M: # 범위 내에 있을 때만 체크
                if (nx // N) == (r_x // N): # 층이 같은 경우
                    if graph[nx][ny] == 0: #안 익은 토마토인 경우만
                        graph[nx][ny] = 1 # 익히기
                        ripen_tomato_cnt += 1 
                        q.append((nx, ny, day + 1))

                else: # 층이 다른 경우
                    if (nx % N) == (r_x % N): # 바로 위 아래 있을 때만 익히기
                        if graph[nx][ny] == 0:
                            graph[nx][ny] = 1 # 익히기
                            ripen_tomato_cnt += 1
                            q.append((nx, ny, day + 1))
    # 토마토를 다 익히지 못하는 경우
    if ripen_tomato_cnt == M*N*H - no_tomato_cnt: 
            print(day)
            return
    else:
        print(-1)
                
bfs()
