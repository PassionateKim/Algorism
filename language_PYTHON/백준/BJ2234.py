# 성곽
# 복습 횟수:0, 01:30:00, 복습필요O
import sys
from collections import defaultdict
si = sys.stdin.readline

M, N = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(N)]

 # 북남서동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def checkWall(val):
    if val == 0:
        return [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 벽: 서 -> 북 남 동
    if val == 1:
        return [[-1, 0], [1, 0], [0, 1]]
    # 벽: 북 -> 남 서 동
    if val == 2:
        return [[1, 0], [0, -1], [0, 1]]
    # 벽: 북, 서 -> 남, 동
    if val == 3: 
        return [[1, 0], [0, 1]]
    # 벽: 동 -> 북, 남, 서
    if val == 4:
        return [[-1, 0], [1, 0], [0, -1]]
    # 벽: 서, 동 -> 북, 남
    if val == 5:
        return [[-1, 0], [1, 0]]
    # 벽: 북, 동 -> 남, 서
    if val == 6:
        return [[1, 0], [0, -1]]
    # 벽: 서, 북, 동 -> 남
    if val == 7:
        return [[1, 0]]
    # 벽: 남 -> 북, 서, 동
    if val == 8:
        return [[-1, 0], [0, -1], [0, 1]]
    # 벽: 남, 서 -> 북, 동
    if val == 9:
        return [[-1, 0], [0, 1]]
    # 벽: 남, 북 -> 서, 동
    if val == 10:
        return [[0, -1], [0, 1]]
    # 벽: 남, 서, 북 -> 동
    if val == 11:
        return [[-1, 0], [0, 1]]
    # 벽: 남, 동 -> 북, 서
    if val == 12:
        return [[-1, 0], [0, -1]]
    # 벽: 남, 서, 동 -> 북
    if val == 13:
        return [[-1, 0]]
    # 벽: 남, 북, 동 -> 서
    if val == 14: 
        return [[0, -1]]
    # 벽: 남, 서, 북, 동
    if val == 15:
        return []

# 다음 기준 벽이 있어서 동쪽으로 못가야하는데 현재 기준으로만 판단하므로
# 오답 
def dfs(x, y, check):
    visited[x][y] = check # 방문처리

    val = graph[x][y]
    wall_list = checkWall(val)

    for x_d, y_d in wall_list:
        nx, ny = x + x_d, y + y_d

        if not (0 <= nx < N and 0 <= ny < M): continue
        if visited[nx][ny] != 0: continue
        
        # 다음 벽 체크
        next_wall_list = checkWall(graph[nx][ny])
        # 없다면 벽이므로
        if [-x_d, -y_d] not in next_wall_list: continue

        dfs(nx, ny, check)    

    return

visited = [[0 for _ in range(M)] for __ in range(N)]

check = 1
for x in range(N):
    for y in range(M):
        if visited[x][y] != 0: continue

        dfs(x, y, check)
        check += 1

# 이방의 개수
print(check-1) 

# 방의 최대
maxi_room_dict = defaultdict(int)

for i in range(N):
    for j in range(M):
        if visited[i][j] not in maxi_room_dict.keys():
            maxi_room_dict[visited[i][j]] = 1
        else:
            maxi_room_dict[visited[i][j]] += 1

print(max(maxi_room_dict.values()))

# 차이나는 위치
diff_set = set()

for x in range(N):
    for y in range(M):
        first = visited[x][y]
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]

            if not (0 <= nx < N and 0 <= ny < M): continue

            if visited[nx][ny] != first:
                tmp = [first, visited[nx][ny]]
                tmp.sort()
                tmp = tuple(tmp)
                diff_set.add(tmp)

maxi = max(maxi_room_dict.values())

for first, second in diff_set:
    tmp = 0
    for x in range(N):
        for y in range(M):
            if visited[x][y] == first or visited[x][y] == second:
                tmp += 1
    maxi = max(maxi, tmp)
print(maxi)