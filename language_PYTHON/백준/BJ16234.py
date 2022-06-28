# 인구 이동
from calendar import c
import sys
from collections import deque
si = sys.stdin.readline

N, L, R = map(int, si().split())
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = [] # 이차원 배열 사용

# 인구 넣기
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)
    
# 비교하기 시간복잡도 O(N^2*4) <= 50 * 50 * 4
answer = 0
cnt = 1
while True:
    check_open = [[0 for i in range(N)] for i in range(N)]
    visited = [[0 for i in range(N)] for i in range(N)] 
    # bfs 시작 - 값 비교해서 연합 구하기
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0: # 방문하지 않은 경우
                visited[i][j] = 1  # 방문처리
                
                q = deque() # bfs 시작 
                q.append((i,j))
                while q:
                    x, y = q.popleft()
                    for idx in range(4):
                        nx, ny = x + dx[idx], y + dy[idx]
                        if not (0<= nx < N and 0<= ny < N): continue # 범위 X 는 나가
                        
                        if L<= abs(graph[x][y] - graph[nx][ny]) <=R: # 두 나라 인구 L명 이상 R명 이하
                            check_open[x][y] = cnt # 연합
                            check_open[nx][ny] = cnt # 연합

                            if visited[nx][ny] == 0: # 방문 X 시
                                visited[nx][ny] = 1 #방문처리
                                q.append((nx, ny))
                cnt += 1

    # 탈출 조건
    flag = 0            
    for i in range(N):
        for j in range(N):
            if check_open[i][j] == 0:
                flag += 1
    
    if flag == N*N:
        print(answer)
        break

    # 연합의 값 초기화 하기
    visited = [[0 for i in range(N)] for i in range(N)] 
    for i in range(N):
        for j in range(N):
            # bfs 시작 
            if check_open[i][j] != 0 and visited[i][j] == 0:
                tmp = check_open[i][j]
                visited[i][j] = 1 # 방문처리
                arr = [(i,j)]
                # 연합 위치 배열 구하기
                q = deque()
                q.append((i,j))
                while q:
                    x, y = q.popleft()
                    for idx in range(4):
                        nx, ny = x + dx[idx], y + dy[idx]
                        if not (0<= nx < N and 0<= ny < N): continue # 범위 X 는 나가

                        if check_open[nx][ny] == tmp and visited[nx][ny] == 0:
                            visited[nx][ny] = 1 # 방문처리
                            q.append((nx,ny))
                            arr.append((nx, ny))

                # 연합의 인구수 구하기
                sumi = 0
                for x, y in arr:
                    sumi += graph[x][y]
                # 초기화 값 구하기
                tmp = sumi // len(arr)

                # graph 값 초기화 하기
                for x, y in arr:
                    graph[x][y] = tmp
                
    answer += 1
