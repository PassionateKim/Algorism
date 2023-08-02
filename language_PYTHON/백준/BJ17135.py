# 캐슬 디펜스
# 복습 횟수:3, 01:30:00, 복습필요3
import sys
import copy
from itertools import combinations
si = sys.stdin.readline 

N, M, D = map(int, si().split())

graph = []
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

answer = 0

archor_position_list = list(combinations(range(M), 3))

def archor_shot(archor):
        # archor 1

    for d in range(1, D+1):
        archor_x, archor_y = N, archor - d # 5, -1
        check = -1
        for i in range(2*d - 1):# d = 3   2d - 1 = 5
                # 중간에서 바꾸기
            if i == d:
                check = (-1) * check
                
            archor_x += check
            archor_y += 1
                # 0 일때 (4, 0)
                # 1 일때 (3, 1)
                # 2 일때 (2, 2)
                # 3 일때 (3, 3)
                # 4 일때 (4, 4)

            if not (0 <= archor_x < N and 0 <= archor_y < M): continue

            if tmp_graph[archor_x][archor_y] == 1:
                target_location_set.add(tuple([archor_x, archor_y]))
                return

for archor1, archor2, archor3 in archor_position_list:

    candidate = 0
    tmp_graph = copy.deepcopy(graph)

    while True:
        # 탈출 조건
        flag = True
        for i in range(N):
            for j in range(M):
                if tmp_graph[i][j] == 1:
                    flag = False
        if flag:
            answer = max(answer, candidate)
            break

        target_location_set = set()
        # 궁수 쏘기
        archor_shot(archor1)
        archor_shot(archor2)
        archor_shot(archor3)


        # 체크 -> 그 부분 적 없애기
        for target_x, target_y in target_location_set:
            candidate += 1
            tmp_graph[target_x][target_y] = 0 # 죽이기
                    

        # 적 내리기
        for i in range(N-2, -1, -1):
            tmp_graph[i+1] = tmp_graph[i]
        tmp_graph[0] = [0] * M

print(answer)