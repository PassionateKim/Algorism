# 함께하는 효도
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)] # 2차원으로 체크하기
x, y = map(int, input().split())
sum_list = []

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(s_x, s_y, depth, sum):
    visited[s_x][s_y] = 1 #방문처리
    # 탈출 조건
    if depth == 3:
        sum_list.append(sum)
        return 
    
    for i in range(4):
        nx = s_x + dx[i]
        ny = s_y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0: #범위 내 & 방문 X 인 경우
            
            dfs(nx, ny, depth+1, sum+graph[nx][ny])
            visited[nx][ny] = 0 # 초기화


    

dfs(x-1, y-1, 0, graph[x-1][y-1])
print(sum_list)