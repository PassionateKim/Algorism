# 치킨 배달
# 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 = sum(치킨거리)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

min_answer = 1e6+1
house_list = []
chicken_list = []
selected_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_list.append((i,j))
        elif graph[i][j] == 2:
            chicken_list.append((i,j))

# Combination 백트레킹으로 구현하기
def dfs(depth, start):
    global min_answer
    if len(selected_list) == M:
        tmp_sum = 0
        for house in house_list:
            chicken_distance = 1e6+1
            for chicken in selected_list:
                chicken_distance = min(chicken_distance, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
            tmp_sum += chicken_distance # 치킨 거리 더하기
        min_answer = min(min_answer, tmp_sum) 
        return
    
    for i in range(start, len(chicken_list)):
        selected_list.append(chicken_list[i])
        dfs(depth+1, i+1)
        selected_list.pop()
            
dfs(0,0)
print(min_answer)

    


    

