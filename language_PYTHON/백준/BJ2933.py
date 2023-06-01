# 미네랄 
# 복습 횟수:1, 01:00:00, 복습필요O
from collections import deque
import sys
si = sys.stdin.readline

R, C = map(int, si().split())
graph = [list(map(str, si().rstrip())) for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(si())
height_list = list(map(int, si().split()))

def check(who, height):
    height = R - height

    if who == 1:
        for y in range(C):
            if graph[height][y] == 'x':
                r, c = height, y
                graph[height][y] = '.'
                break
    
    else:
        for y in range(C-1, -1, -1):
            if graph[height][y] == 'x':
                r, c = height, y
                graph[height][y] = '.'
                break


    if(r + c) != -2:
        for idx in range(4):
            nr, nc = r + dx[idx], c + dy[idx]
            if not ( 0 <= nr < R and 0 <= nc < C): continue

            if graph[nr][nc] == 'x':
                candidate.append([nr, nc])
    
    return


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1 # 방문 처리
    fall_list = []

    while q:
        x, y = q.popleft()
    
        # x의 위치가 땅이라면 떨어질 수 없으므로 return
        if x == R - 1:
            return

        if graph[x+1][y] == '.':
            fall_list.append([x, y])
        
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]

            if not (0 <= nx < R and 0 <= ny < C): continue

            if visited[nx][ny] == 0 and graph[nx][ny] == 'x':
                q.append([nx, ny])
                visited[nx][ny] = 1 # 방문 처리
    
    fall(fall_list)

    return

def fall(fall_list):
    k = 1
    flag = 0
    # 한칸씩 더 내려가며 최대 치를 체크한다.
    while True:
        for x, y in fall_list:
            if x + k == R - 1:
                flag = 1
                break
            
            # cluster가 아니면서 벽인 경우
            if graph[x + k + 1][y] == 'x' and visited[x + k + 1][y] == 0:
                flag = 1
                break
        
        if flag:
            break

        k += 1
    
    for x in range(R-1, -1, -1):
        for y in range(C):
            if visited[x][y] == 1 and graph[x][y] == 'x':
                graph[x][y] = '.'
                graph[x+k][y] = 'x'
    
    return


who = 1
for height in height_list:
    candidate = []
    check(who, height)
    # bfs로 클러스터 찾기
    for x, y in candidate:
        visited = [[0 for _ in range(C)] for _ in range(R)]
        bfs(x, y)

    who = -1 * who

for i in graph:
    print("".join(i))