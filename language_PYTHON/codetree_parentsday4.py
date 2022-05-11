# 함께하는 효도
# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(m)]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

visited = [[False] * n for _ in range(n)]
ans = 0
selected_nums = []

# 격자 밖을 나가는지 확인합니다.
def is_out_range(x, y):
    return not (0 <= x and x < n and 0 <= y and y < n)


def count_max_fruit(cnt):
    # (3 * m) 개의 방향을 모두 뽑은 경우 총량을 계산합니다.
    if cnt == 3 * m:
        # visited 배열을 초기화합니다.
        for i in range(n):
            for j in range(n): visited[i][j] = False
        
        for i in range(m):
            cx = a[i][0] - 1
            cy = a[i][1] - 1
            visited[cx][cy] = True # 방문 처리를 합니다.
            nx = cx
            ny = cy
            for j in range(3):
                nx += dxs[selected_nums[i * 3 + j]]
                ny += dys[selected_nums[i * 3 + j]]

                # 만약 하나라도 격자 밖을 나갈 경우,
                # 불가능한 이동이기 때문에 즉시 리턴합니다.
                if is_out_range(nx, ny):
                    return

                visited[nx][ny] = True

        val = 0
        # 방문한 적 있는 모든 위치의 수확량을 더해 총량을 계산합니다.
        for i in range(n):
            for j in range(n):
                if visited[i][j]: val += board[i][j]
        global ans
        ans = max(ans, val)
        return

    # 상하좌우 4가지 방향에 대해 탐색합니다.
    for dir in range(4):
        selected_nums.append(dir)
        count_max_fruit(cnt + 1)
        selected_nums.pop()


count_max_fruit(0)

# 정답을 출력합니다.
print(ans)












 
 
 
#  import sys

# n, m = map(int, sys.stdin.readline().split())

# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# visited = [[0] * n for _ in range(n)] # 2차원으로 체크하기
# x, y = map(int, input().split())
# sum_list = []

# # 상하좌우
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def dfs(s_x, s_y, depth, sum):
#     visited[s_x][s_y] = 1 #방문처리
#     # 탈출 조건
#     if depth == 3:
#         sum_list.append(sum)
#         return 
    
#     for i in range(4):
#         nx = s_x + dx[i]
#         ny = s_y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0: #범위 내 & 방문 X 인 경우
            
#             dfs(nx, ny, depth+1, sum+graph[nx][ny])
#             visited[nx][ny] = 0 # 초기화


    

# dfs(x-1, y-1, 0, graph[x-1][y-1])
# print(sum_list)