# 치킨 배달
# 복습 횟수:3, 00:15:00, 복습필요X
import sys
from itertools import combinations
si = sys.stdin.readline
N, M = map(int, si().split())
graph = []
for i in range(N):
    graph.append(list(map(int, si().split())))
answer = sys.maxsize
chicken_list = []
house_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_list.append([i, j])
        if graph[i][j] == 2:
            chicken_list.append([i, j])

chicken_list_combi = list(combinations(chicken_list, M))
for chicken_list in chicken_list_combi:
    tmp_sum = 0
    for house_x, house_y in house_list:
        c_d = sys.maxsize
        for chicken_x, chicken_y in chicken_list:
            c_d = min(abs(house_x - chicken_x) + abs(house_y - chicken_y), c_d)
        tmp_sum += c_d
    answer = min(answer, tmp_sum)

print(answer)