# 안전 영역
import sys
si = sys.stdin.readline

N = int(si())
# 상하좌우
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 1. 2차원 그래프 생성하기
graph = [[] for i in range(N)]
answer = -1
maxi = -1
for i in range(N):
    tmp = list(map(int, si().split()))
    graph[i] = tmp

# 2차원 그래프의 최댓값 체크하기
for i in graph:
    a = max(i)
    maxi = max(maxi, a)
def dfs(x, y, visited, check_graph):
    visited[x][y] = 1 # 방문처리
    for dir in dirs:
        nx = x + dir[0]
        ny = y + dir[1]

        if (0 <= nx < N and 0 <= ny < N):
            if (visited[nx][ny] == 0):
                if (check_graph[nx][ny] == 0):
                    dfs(nx, ny, visited, check_graph)



for rain in range(1, maxi):
    # 물에 잠긴 부분 check를 위한 graph
    check_graph = [[0 for i in range(N)] for i in range(N)]
    
    # 2.1 rain 에 따라 잠기는 부분 체크하기
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= rain:
                check_graph[i][j] = 1 # 잠긴 부분 체크하기
    
    
    # 2.2 visited graph 체크하기
    cnt = 0
    visited = [[0 for i in range(N)] for i in range(N)]

    for x in range(N):
        for y in range(N):
            if visited[x][y] == 1: continue # 방문한 적이 없고
            if check_graph[x][y] == 1: continue # 물에 잠기지 않은 부분이라면
            
            cnt += 1
            dfs(x, y, visited, check_graph) 

    answer = max(answer, cnt)

print(answer)   


            






