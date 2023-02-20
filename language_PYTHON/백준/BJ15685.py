# 드래곤 커브
# 복습 횟수:2, 01:45:00, 복습필요X
import sys
from collections import deque
si = sys.stdin.readline
N = int(si())

graph = [[0 for _ in range(101)] for __ in range(101)]
dragon_list = deque()

for i in range(N):
    tmp = list(map(int, si().split()))
    dragon_list.append(tmp)

def initDragonList(x, y, d, q: deque):
    if d == 0:
        graph[x][y+1] = 1 # 방문처리
        q.append([x, y+1, d])
    elif d == 1:
        graph[x-1][y] = 1 # 방문처리
        q.append([x-1, y, d])
    elif d == 2:
        graph[x][y-1] = 1
        q.append([x, y-1, d])
    else: # d == 3:
        graph[x+1][y] = 1 
        q.append([x+1, y, d])
    return

def converter(q: deque):
    for i in range(len(q)-1, 0, -1):
        x, y = q[-1][0], q[-1][1] # 좌표는 끝점을 기준으로
        dir = q[i][2] # 방향은 i를 기준으로
        
        if dir == 0: # 좌 -> 우 이므로
            q.append([x-1, y, 1])
            graph[x-1][y] = 1 # 방문처리
        elif dir == 1: # 하 -> 상 이므로
            q.append([x, y-1, 2])
            graph[x][y-1] = 1 # 방문처리
        elif dir == 2: # 우 -> 좌 이므로
            q.append([x+1, y, 3])
            graph[x+1][y] = 1 # 방문처리
        else: # dir == 3: # 상 -> 하 이므로
            q.append([x, y+1, 0])
            graph[x][y+1] = 1 # 방문처리

    return

while dragon_list:
    y, x, d, g = dragon_list.pop() # 편의상 y, x 스왑
    q = deque()
    q.append([x, y, d])
    graph[x][y] = 1 # 방문처리
    initDragonList(x, y, d, q) # 0세대 초기화

    for i in range(g):
        converter(q)

answer = 0
dir = [(0, 0), (0, 1), (1, 0), (1, 1)]
for x in range(100):
    for y in range(100):
        tmp = 0
        for idx in range(4):
            nx, ny = x + dir[idx][0], y + dir[idx][1]
            if graph[nx][ny] == 1:
                tmp += 1
        
        if tmp == 4: # 정사각형이므로
            answer += 1

print(answer)