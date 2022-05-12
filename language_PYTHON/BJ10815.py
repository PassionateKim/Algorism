# 치킨 배달
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

house_list = []
chicken_list = []
choosen_chicken_list = []
answer = 1000
# 치킨집, 집 위치 값 넣기
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken_list.append((i,j))
        if graph[i][j] == 1:
            house_list.append((i,j))

# dfs 구현
def dfs(depth, idx):
    global answer
    if depth == M:
        sum = 0
        for house in house_list:
            val = 1000
            for choosen_chicken in choosen_chicken_list:
                tmp = abs(house[0]-choosen_chicken[0]) + abs(house[1]-choosen_chicken[1])
                val = min(tmp, val)
            sum += val
        answer = min(answer, sum)  
        return

    for i in range(idx, len(chicken_list)):
        if chicken_list[i] in choosen_chicken_list:
            continue
        
        choosen_chicken_list.append(chicken_list[i])
        dfs(depth+1, i+1)
        choosen_chicken_list.pop()
        
dfs(0, 0)
print(answer)

        
        


