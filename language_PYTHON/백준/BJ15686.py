# 2022-05-13
# 2022-06-05
# 2022-07-27
# 치킨 배달
from re import L
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(N)]

chicken_list = []
house_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_list.append([i,j])
        elif graph[i][j] == 2:
            chicken_list.append([i,j])

answer = 1e10
def dfs(idx, arr : list):
    global answer
    if len(arr) == M:
        city_d = 0
        # 집 in 집_list:
        for house in house_list:
            hx, hy = house[0], house[1]
            chicken_d = 1e10
            for chicken in arr:
                cx, cy = chicken[0], chicken[1]
                tmp = abs(hx- cx) + abs(hy - cy)
                
                # 치킨 거리 구하기
                chicken_d = min(chicken_d, tmp)
            # 치킨 거리 더하기
            city_d += chicken_d
        # / 집 list
        answer = min(city_d, answer)
        return

    for i in range(idx, len(chicken_list)):
        arr.append(chicken_list[i])
        dfs(i+1, arr)
        arr.pop()

dfs(0, [])
print(answer)