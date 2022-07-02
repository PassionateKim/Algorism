# 마법사 상어와 블리자드
import sys
from collections import deque
si = sys.stdin.readline

dir = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
graph = []
m_list = []

N, M = map(int, si().split())

for i in range(N):
    graph.append(list(map(int, si().split())))

for i in range(M):
    m_list.append(list(map(int, si().split())))

# 비바라기 시전 초기화
cloud = deque([(N-2, 0), (N-2, 1),(N-1, 0), (N-1, 1)])
for idx, s in m_list: # 방향, 거리

    
    tmp = deque()
    # 1단계 구름 위치 옮기기    
    while cloud:# 이동 후 구름 위치
        x, y = cloud.popleft() # 여긴 인덱스로 바꿔야해서 -1
        nx, ny = x + dir[idx-1][0] * (s) , y + dir[idx-1][1] * (s)
        #  1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다
        if nx < 0:
            nx = nx % N
            # while True:
            #     nx = nx + N  # - 3 -> 2
            #     if nx >= 0:
            #         break
        if nx >= N:
            nx = nx % N
            # while True:
            #     nx = nx - N  # 5 -> 0
            #     if nx < N:
            #         break
        if ny < 0:
            ny = ny % N
            # a = abs(ny)
            # b = a % N
            # by = N - a
            # while True:
            #     ny = ny + N
            #     if ny >= 0:
            #         break
        if ny >= N:
            ny = ny % N
            # while True:
            #     ny = ny - N
            #     if ny < N:
            #         break 
        tmp.append((nx, ny)) # 이동 후 구름 위치
    # print(tmp)
    # 2,3단계 저장된 물 1 증가시키기 구름이 모두 사라진다
    arr = deque()
    while tmp:
        x, y = tmp.popleft()
        graph[x][y] += 1
        arr.append((x,y))
    

    # 4단계 대각선 물 체크
    visited = [[0 for _ in range(N)] for __ in range(N)]
    while arr:
        x, y = arr.popleft()
        visited[x][y] = 1 #방문처리 for 5단계
        cnt = 0
        for idx in range(1, 8, 2): # 직접 인덱스 1 3 5 7 대각선
            nx, ny = x + dir[idx][0], y + dir[idx][1]
            if not (0<=nx<N and 0<=ny<N): continue # 범위 넘으면 X 

            if graph[nx][ny] > 0: # 물이 있으면
                cnt += 1 
        graph[x][y] += cnt

    
    # 5단계
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1: continue # 구름이 있었던 칸 제외

            if graph[i][j] >= 2:
                cloud.append((i,j)) # 구름이 생긴다
                graph[i][j] -= 2 #  물의 양이 2만큼 줄어든다.   
    
# 더하기
answer = 0
for i in range(N):
    for j in range(N):
        answer += graph[i][j]
print(answer)

# // % 헷갈리지 말것.