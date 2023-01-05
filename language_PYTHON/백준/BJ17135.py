# 캐슬 디펜스
import sys
import copy
from itertools import combinations

si = sys.stdin.readline
N, M, D = map(int, si().split())
graph = []
answer = 0

for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

archor_location_list = list(combinations(range(M), 3))
#1. 각 combination case 마다 while 문으로 탐색
for archor_location in archor_location_list:
    x, y, z = archor_location
    archor1 = [N, x]
    archor2 = [N, y]
    archor3 = [N, z]
    enemy_set = set() # 중복은 되지 않으므로
    tmp_graph = copy.deepcopy(graph)
    candidate = 0
    while True:
        # if all 0  (적이 없는 경우 종료)
        flag = 1 
        for i in range(N):
            for j in range(M):
                if tmp_graph[i][j] == 1:
                    flag = 0
        if flag:
            break

        # 2. 탐색 시작 archor1
        check1 = 0
        for d in range(1, D+1):
            
            archor1_x = archor1[0] # 세로 위치
            archor1_y = archor1[1] # 가로 위치 y
            diff = d 
            archor1_y = archor1_y - diff 
            tmp = -1
            
            for idx in range(2*d-1):
                archor1_x += tmp 
                archor1_y += 1  

                if archor1_x == (N-d):
                    tmp = 1
                
                # 범위 외는 continue
                if not (0 <= archor1_x < N and 0 <= archor1_y < M): continue

                # enemy 인지 체크
                if tmp_graph[archor1_x][archor1_y] == 1:
                    enemy_set.add((archor1_x, archor1_y)) # 중복으로 한번에 쏠 수 있으므로
                    check1 = 1
                    break
            if check1:
                break
        
        check2 = 0
        for d in range(1, D+1):
            # archor2
            archor2_x = archor2[0] # 세로 위치
            archor2_y = archor2[1] #가로 위치 y
            diff = d 
            archor2_y = archor2_y - diff 
            tmp = -1
            
            for idx in range(2*d-1):
                archor2_x += tmp 
                archor2_y += 1  

                if archor2_x == (N-d):
                    tmp = 1
                
                # 범위 외는 continue
                if not (0 <= archor2_x < N and 0 <= archor2_y < M): continue

                # enemy 인지 체크
                if tmp_graph[archor2_x][archor2_y] == 1:
                    enemy_set.add((archor2_x, archor2_y)) # 중복으로 한번에 쏠 수 있으므로
                    check2 = 1
                    break
            if check2:
                break
            
        # archor3
        check3 = 0
        for d in range(1, D+1):
            archor3_x = archor3[0] # 세로 위치
            archor3_y = archor3[1] # 가로 위치 y
            diff = d 
            archor3_y = archor3_y - diff 
            tmp = -1
            
            for idx in range(2*d-1):
                archor3_x += tmp 
                archor3_y += 1  

                if archor3_x == (N-d):
                    tmp = 1
                
                # 범위 외는 continue
                if not (0 <= archor3_x < N and 0 <= archor3_y < M): continue

                # enemy 인지 체크
                if tmp_graph[archor3_x][archor3_y] == 1:
                    enemy_set.add((archor3_x, archor3_y)) # 중복으로 한번에 쏠 수 있으므로
                    check3 = 1
                    break
            if check3:
                break
        
        while enemy_set:
            x,y = enemy_set.pop()
            tmp_graph[x][y] = 0 
            candidate += 1
        
        # graph 초기화
        # 초기화-1 아래로 내리기
        for i in range(N-2, -1, -1):
            for j in range(M):
                tmp_graph[i+1][j] = tmp_graph[i][j]
        # 초기화-2 맨위 모두 0으로 초기화
        for j in range(M):
            tmp_graph[0][j] = 0 

    answer = max(answer, candidate)    

print(answer)