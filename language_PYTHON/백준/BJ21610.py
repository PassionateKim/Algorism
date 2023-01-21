# 마법사 상어와 비바라기
# 복습 횟수:2, 02:00:00
import sys
si = sys.stdin.readline

N, M = map(int, si().split())
graph = []
move = []
dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
dir2 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

for i in range(M):
    tmp = list(map(int ,si().split()))
    move.append(tmp)

def changeLocation(tmp_list : list):
    while tmp_list[0] >= N:
        tmp_list[0] = tmp_list[0] - N
    while tmp_list[1] >= N:
        tmp_list[1] = tmp_list[1] - N
    while tmp_list[0] < 0:
        tmp_list[0] = tmp_list[0] + N
    while tmp_list[1] < 0:
        tmp_list[1] = tmp_list[1] + N
        
    return tmp_list

def converter(cloud_list : list, turn, distance):
    new_cloud_list = []

    while cloud_list:
        x, y = cloud_list.pop()
        new_x, new_y = x + dir[turn][0] * distance, y + dir[turn][1] * distance  
        
        new_cloud = changeLocation([new_x, new_y])
        new_cloud_list.append(new_cloud)
        
    return new_cloud_list

# move 시작
cloud_list = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for i in range(M):
    # 구름 이동시키기
    visited = [[0 for i in range(N)] for i in range(N)]
    turn, distance = move[i][0] -1, move[i][1]
    cloud_list = converter(cloud_list, turn, distance)

    # 물 뿌리기
    for cloud in cloud_list:
        x, y = cloud
        graph[x][y] = graph[x][y] + 1

    # 대각선 체크하기
    for cloud in cloud_list:
        x, y = cloud
        navi = []

        for i in range(4):
            nx, ny = x + dir2[i][0], y + dir2[i][1]
            if not (0 <= nx < N and 0 <= ny < N): continue
            
            navi.append([nx, ny])

        for nav in navi:
            x2, y2 = nav
            if graph[x2][y2] != 0:
                graph[x][y] = graph[x][y] + 1
    
    # 기존 구름 위치 체크
    while cloud_list:
        x, y = cloud_list.pop()
        visited[x][y] = 1 # 방문처리
    
    # 물 넣기
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1: continue # 구름이 기존에 있던 자리는 제외한다
            if graph[i][j] < 2: continue # 물의 양이 2 이상인 칸에 구름이 생긴다

            cloud_list.append([i, j])
            graph[i][j] = graph[i][j] - 2 # 구름이 생성되면 물의 양이 2만큼 줄어든다.

answer = 0
for i in graph:
    answer += sum(i)

print(answer)