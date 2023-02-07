# 이차원 배열과 연산
# 복습 횟수:0, 02:15:00, 복습필요O
import sys
from collections import deque
import copy
si = sys.stdin.readline
r, c, K = map(int, si().split())
r, c  = r - 1, c - 1
graph = []
for i in range(3):
    graph.append(list(map(int, si().split())))

answer = 0
while True:
    # 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
    # 행이 넘어가는 경우
    if len(graph) > 100:
        new_graph = []
        for i in range(100):
            new_graph.append(graph[i])
        graph = copy.deepcopy(new_graph)
    # 열이 넘어가는 경우
    if len(graph[0]) > 100:
        new_graph = []
        for i in range(len(graph)):
            new_graph.append(graph[i][:100])
        graph = copy.deepcopy(new_graph)

    # 조건을 만족하면
    if len(graph)-1 >= r and len(graph[0])-1 >= c and graph[r][c] == K:
        print(answer)
        break
    # 100초가 지나도 A[r][c] == K 가 되지 않으면 -1을 출력한다.
    if answer == 100:
        print(-1)
        break
    
    N, M = len(graph), len(graph[0])
    if N >= M: # 행의 개수 >= 열의 개수 배열 A의 모든 행에 대해 정렬을 수행함
        candidate = list()
        for i in range(len(graph)):
            num_set = set(graph[i])
            can = []
            for num in num_set: # graph[i] 행에서의 개수를 본다.
                if num == 101: continue
                cnt = graph[i].count(num)
                can.append([num, cnt])
            can.sort(key=lambda x: (x[1], x[0])) # 정렬
            # flat 하게 변경
            flated = []
            for num, cnt in can:
                flated.append(num)
                flated.append(cnt)
            candidate.append(flated)
        # 0(101)으로 넣기
        max_yeol = 0
        # max_yeol 구하기
        for i in range(len(candidate)):
            max_yeol = max(max_yeol, len(candidate[i]))
        # 101로 채워넣기
        for i in range(len(candidate)):
            size = len(candidate[i])
            for j in range(max_yeol - size):
                candidate[i].append(101)

        # graph 초기화
        graph = copy.deepcopy(candidate)
    else: # C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우
        candidate = list()
        for i in range(len(graph[0])):
            target_list = list()
            for j in range(len(graph)):
                target_list.append(graph[j][i])
            num_set = set(target_list)
            can = []
            for num in num_set: # 열에서의 개수를 본다.
                if num == 101: continue
                cnt = target_list.count(num)
                can.append([num, cnt])
            can.sort(key=lambda x: (x[1], x[0])) # 정렬
            # flat 하게 변경
            flated = []
            for num, cnt in can:
                flated.append(num)
                flated.append(cnt)
            candidate.append(flated)
        # 0(101)으로 넣기
        max_yeol = 0
        # max_hang 구하기
        for i in range(len(candidate)):
            max_yeol = max(max_yeol, len(candidate[i]))
        # 101로 채워넣기
        for i in range(len(candidate)):
            size = len(candidate[i])
            for j in range(max_yeol - size):
                candidate[i].append(101)

        # graph 초기화
        graph = []
        for i in range(len(candidate[0])):
            tmp = []
            for j in range(len(candidate)):
                tmp.append(candidate[j][i])
            graph.append(tmp)

    answer += 1