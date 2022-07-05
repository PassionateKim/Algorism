# 마법사 상어와 비바라기
from shutil import move
import sys
si = sys.stdin.readline

N, M = map(int, si().split())
graph = []
dir = [0, (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
command = []
# 그래프 만들기
for i in range(N):
    graph.append(list(map(int, si().split())))
# 커맨드
for i in range(M):
    command.append(list(map(int, si().split())))

cloud_location = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]


def move_cloud(idx, distance, cloud_location):
    tmp = []
        
    # dir[idx]
    for cloud in cloud_location:
        nx, ny = cloud[0] + (dir[idx][0] * (distance%N)), cloud[1] + (dir[idx][1] * (distance%N))
        
        if nx < 0:
            nx += N
        elif nx >= N:
            nx -= N
        
        if ny < 0:
            ny += N
        elif ny >= N:
            ny -= N
        
        tmp.append((nx, ny))
    return tmp
    

for cmd in command:
    idx, dist = cmd[0], cmd[1]
    
    # 1 단계 - 구름 이동 시키기
    after_cloud_location = move_cloud(idx, dist, cloud_location)
    
    # 2 단계 - 물 추가하기
    for cloud in after_cloud_location:
        x, y = cloud[0], cloud[1]
        graph[x][y] += 1 # 1 추가하기
    
    # 3 단계 - 물 복사하기
    for cloud in after_cloud_location:
        x, y = cloud[0], cloud[1]
        
        # 상하좌우
        for idx in range(2, 9, 2):
            nx, ny = x + dir[idx][0], y + dir[idx][1]
            if not (0<=nx<N and 0<=ny<N): continue # 범위밖 X

            if graph[nx][ny] != 0: # 물이 있다면
                graph[x][y] += 1 # 물 추가

    # 4 단계 구름이 있었던 칸을 제외한 나머지 칸 중 물의 양이 2이상인 칸에 구름
    # 4.1 구름 위치 체크
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for cloud in after_cloud_location:
        x, y = cloud[0], cloud[1]
        visited[x][y] = 1 # 방문 처리

    # 4.2 구름 위치 제외 후 물 양 2이면 구름 추가
    cloud_location.clear() # 삭제!
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1: continue # 구름 위치 제외

            if graph[i][j] >= 2:
                cloud_location.append((i, j)) # 위치 추가
                graph[i][j] -= 2 # 물의 양 2만큼 준다.
    
answer = 0
for i in range(N):
    for j in range(N):
        answer += graph[i][j]
print(answer)
