# 캐슬 디펜스
# 복습 횟수:2, 01:00:00, 복습필요O
import sys
import copy
from itertools import combinations
si = sys.stdin.readline
N, M, D = map(int, si().split())

can_graph = []
for i in range(N):
    can_graph.append(list(map(int, si().split())))

archor_combi = list(combinations(range(M), 3))
answer = 0
for arch1, arch2, arch3 in archor_combi:
    graph = copy.deepcopy(can_graph)

    tmp = 0
    while True: 
        enemy_list = dict()
        # 탈출 조건
        check = 1
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1:
                    check = 0
        if check:
            break
        
        flag = 0
        # arch1
        for distance in range(1, D+1): # 1, 2, 3
            x, y = N, arch1 - distance
            diff = -1
            for d in range(distance * 2 - 1): # 맨해튼 거리로 풀기
                if x == N - (distance):
                    diff = 1

                x = x + diff
                y = y + 1

                if not (0 <= x < N and 0 <= y < M): continue # 범위 밖은 out

                if graph[x][y] == 1: #적이라면 쏜다
                    enemy_list[(x, y)] = 1
                    flag = 1
                
                if flag:
                    break
            if flag:
                break
        
        flag = 0    
        # arch2
        for distance in range(1, D+1): # 1, 2, 3
            x, y = N, arch2 - distance
            diff = -1
            for d in range(distance * 2 - 1): # 맨해튼 거리로 풀기
                if x == N - (distance):
                    diff = 1

                x = x + diff
                y = y + 1

                if not (0 <= x < N and 0 <= y < M): continue # 범위 밖은 out

                if graph[x][y] == 1: #적이라면 쏜다
                    enemy_list[(x, y)] = 1
                    flag = 1
                
                if flag:
                    break
            if flag:
                break
        
        flag = 0
        # arch3
        for distance in range(1, D+1): # 1, 2, 3
            x, y = N, arch3 - distance
            diff = -1
            for d in range(distance * 2 - 1): # 맨해튼 거리로 풀기
                if x == N - (distance):
                    diff = 1

                x = x + diff
                y = y + 1

                if not (0 <= x < N and 0 <= y < M): continue # 범위 밖은 out

                if graph[x][y] == 1: #적이라면 쏜다
                    enemy_list[(x, y)] = 1
                    flag = 1
                
                if flag:
                    break
            if flag:
                break
        
        for x, y in enemy_list.keys():
            tmp += 1
            graph[x][y] = 0 # 죽이기
        
        for i in range(N-2, -1, -1):
            graph[i+1] = graph[i]

        graph[0] = [0] * M

    answer = max(answer, tmp)

print(answer)