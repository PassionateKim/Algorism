# 캐슬 디펜스
# 복습 횟수:1, 01:30:00, 복습필요O
import sys
from itertools import combinations
si = sys.stdin.readline

N, M, D = map(int, si().split())
main_graph = []

for i in range(N):
    tmp = list(map(int, si().split()))
    main_graph.append(tmp)

answer = 0
archor_list = list(combinations(range(M), 3))

for archor in archor_list:
    tmp = 0
    archor1, archor2, archor3 = archor
    cnt = 0
    graph = [[0 for _ in range(M)] for __ in range(N)]
    for i in range(N):
        for j in range(M):
            graph[i][j] = main_graph[i][j]

    while True:
        mob_set = set() # 중복 가능하므로

        if cnt > N: break
        # archor 1
        flag = 0
        for d in range(1, D+1):
            diff = -1
            x = N
            y = archor1 - d
            # 궁수가 쏘는 mob 위치 탐색
            for i in range(d*2-1):
                if x == N-d:
                    diff = 1

                x = x + diff 
                y = y + 1
                if not (0 <= x < N and 0 <= y < M): continue # 범위밖은 생략
                if graph[x][y] == 0: continue # mob 없으면 생략

                if graph[x][y] == 1: # mob이 있다면
                    mob_set.add((x, y))
                    flag = 1
                
                if flag:
                    break
            if flag:
                break

        # archor 2
        flag = 0
        for d in range(1, D+1):
            diff = -1
            x = N
            y = archor2 - d
            # 궁수가 쏘는 mob 위치 탐색
            for i in range(d*2-1):
                if x == N-d:
                    diff = 1

                x = x + diff 
                y = y + 1

                if not (0 <= x < N and 0 <= y < M): continue # 범위밖은 생략
                if graph[x][y] == 0: continue # mob 없으면 생

                if graph[x][y] == 1: # mob이 있다면
                    mob_set.add((x, y))
                    flag = 1
                
                if flag:
                    break
            if flag:
                break

        # archor 3
        flag = 0
        for d in range(1, D+1):
            diff = -1
            x = N
            y = archor3 - d
            # 궁수가 쏘는 mob 위치 탐색
            for i in range(d*2-1):
                if x == N-d:
                    diff = 1

                x = x + diff 
                y = y + 1

                if not (0 <= x < N and 0 <= y < M): continue # 범위밖은 생략
                if graph[x][y] == 0: continue # mob 없으면 생

                if graph[x][y] == 1: # mob이 있다면
                    mob_set.add((x, y))
                    flag = 1
                
                if flag:
                    break
            if flag:
                break
        # mob 제거하기
        while mob_set:
            x, y = mob_set.pop()
            tmp += 1
            graph[x][y] = 0

        # 한 칸 내리기
        for i in range(N-2, -1, -1):
            graph[i+1] = graph[i]
        
        graph[0] = [0] * M
        cnt += 1

    answer = max(answer ,tmp)
    
print(answer)