# 치킨 배달
import sys
si = sys.stdin.readline

N, M = map(int, si().split())
graph = []
chicken_list = []
house_list = []
for i in range(N):
    graph.append(list(map(int, si().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: # 집이면
            house_list.append((i,j))
        elif graph[i][j] == 2: # 치킨집이면
            chicken_list.append((i,j))
answer = 1e10
def dfs(depth, l : list, idx):
    # global answer
    # # 탈출 조건
    # if len(l) == M: 
    #     sumi_dis = 0 # 도시의 치킨 거리
    #     for house in house_list:
    #         dis = 1e9
    #         h_x, h_y = house[0], house[1]
    #         for chicken in l: # 치킨거리
    #             c_x, c_y = chicken[0], chicken[1]
    #             differ = abs(h_x - c_x) + abs(h_y - c_y)
    #             dis = min(dis, differ)
    #         sumi_dis += dis
    #     # 최소 비교
    #     answer = min(answer, sumi_dis)
    #     return
    if len(l) == M:
        print(l)
        return

    for i in range(idx, len(chicken_list)):
        chicken = chicken_list[i]
        l.append(chicken)
        dfs(depth+1, l, idx+1)
        l.pop()

dfs(0, [], 0)

