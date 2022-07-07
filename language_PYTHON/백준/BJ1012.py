#유기농 배추
from calendar import c
import sys
si = sys.stdin.readline

dir = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs(x, y):
    visited[x][y] = 1 # 방문처리

    for idx in range(4):
        nx, ny = x + dir[idx][0], y + dir[idx][1]
        if not (0<=nx<N and 0<=ny<M): continue # 범위 밖 X
        if visited[nx][ny] == 1: continue # 이미 방문 시 X

        if graph[nx][ny] == 1:
            dfs(nx, ny)
    return


T = int(si())
for i in range(T):
    M, N, K = map(int, si().split())
    graph = [[0 for i in range(M)] for _ in range(N)]
    visited = [[0 for i in range(M)] for _ in range(N)]
    #배추 위치 초기화
    for i in range(K):
        y, x = map(int, si().split())
        graph[x][y] = 1 
    
    # DFS로 배추위치 탐색 시작
    answer = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and graph[i][j] == 1: # 배추 위치 
                dfs(i, j)
                answer += 1
    print(answer)
        
