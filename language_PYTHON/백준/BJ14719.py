# 빗물
import sys
si = sys.stdin.readline

answer = 0
N, M = map(int, si().split())
height_list = list(map(int, si().split())) # 3 1 2 3 4 1 1 2
graph = [[0 for _ in range(M)] for __ in range(N)]

# 벽 초기화
for i in range(len(height_list)):
    for j in range(N-1, (N-1) - height_list[i], -1):
        graph[j][i] = 1 # 벽은 1으로 한다.

# 탐색 시작
for i in range(N-1, -1, -1): # 1층부터 탐색 3 -> 2 -> 1 -> 0
    # 첫번째가 기둥인지 아닌지
    if graph[i][0] == 1: 
        isFirstWall = True
    else: 
        isFirstWall = False
    
    tmp = 0
    for j in range(1, M): # 우측으로 가면서 체크 0 -> 1 -> 2 -> 3 -> 4 ...
        if isFirstWall: # 첫번째가 기둥이면 count가 가능하다.
            if graph[i][j] == 0: # 물을 담을 수 있다면
                tmp += 1
            else: # 벽이라면
                answer += tmp
                tmp = 0
        else: # 첫번째가 기둥이 아니라면 다음 기둥을 찾아야 한다.
            if graph[i][j] == 1:
                isFirstWall = True

print(answer)