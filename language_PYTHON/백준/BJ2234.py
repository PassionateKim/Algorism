# 성곽
# 복습 횟수:1, 01:00:00, 복습필요O
import sys
from collections import defaultdict
si = sys.stdin.readline

M, N = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for __ in range(N)]

# 남 동 북 서
# graph 모양 치환
for i in range(N):
    for j in range(M):
        info = bin(graph[i][j])[2:] # 이진수로 변환하는 함수
        info = '0' * (4 - len(info)) + info # 자리수 맞춰주기
        graph[i][j] = list(map(int, info))

def getNewLocation(x, y, idx):
    # 남쪽
    if idx == 0:
        return x+1, y
    # 동쪽
    if idx == 1:
        return x, y+1
    # 북쪽
    if idx == 2:
        return x-1, y 
    # 서쪽
    if idx == 3:
        return x, y-1 

def changeDir(idx):
    if idx == 0:
        return 2
    if idx == 1:
        return 3
    if idx == 2:
        return 0
    if idx == 3:
        return 1
    
def dfs(x, y, check):
    visited[x][y] = check # 방문 처리

    target = graph[x][y]
    
    for idx in range(4):
        if target[idx] == 1: continue

        nx, ny = getNewLocation(x, y, idx)
        if not (0 <= nx < N and 0 <= ny < M): continue
        if visited[nx][ny] != 0: continue

        # 가려는 방향의 벽도 체크해야함
        next_target = graph[nx][ny]
        dir = changeDir(idx)
        if next_target[dir] == 1: continue

        dfs(nx, ny, check)

    return

check = 1
# 1. 방 나누기
for i in range(N):
    for j in range(M):
        if visited[i][j] != 0: continue

        dfs(i, j, check)
        check += 1

print(check - 1)
# 2. 가장 넓은 방의 넓이
room_size_dict = defaultdict(int)

for i in range(N):
    for j in range(M):
        val = visited[i][j]

        if val not in room_size_dict.keys():
            room_size_dict[val] = 1
        else:
            room_size_dict[val] += 1

print(max(room_size_dict.values()))

# 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
maxi = max(room_size_dict.values())
diff_set = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(N):
    for y in range(M):
        check = visited[x][y]

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]

            if not (0 <= nx < N and 0 <= ny < M): continue

            if check != visited[nx][ny]:
                tmp = [check, visited[nx][ny]]
                tmp.sort()

                diff_set.add(tuple(tmp))

# 전체를 돌면서 합쳐지는 방 숫자를 가진 것의 총 개수 체크
for x, y in diff_set:
    tmp = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == x or visited[i][j] == y:
                tmp += 1
    
    maxi = max(maxi, tmp)
print(maxi)