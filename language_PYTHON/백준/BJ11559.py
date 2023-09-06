import sys
from collections import deque

si = sys.stdin.readline 
graph = []
for i in range(12):
    tmp = list(map(str, si().rstrip()))
    graph.append(tmp)

answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def pop_puyo():

    return

# 뿌요 체크
def check_puyo_bfs():
    visited = [[0 for i in range(6)] for i in range(12)]

    for i in range(12):
        for j in range(6):
            if graph[i][j] == '.': continue
            if visited[i][j] == 1: continue
            bfs2(i, j, visited)

    return

def bfs2(x, y, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1 # 방문 처리
    puyo = graph[x][y]

    candidate_list = []
    candidate_list.append([x, y])
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not ( 0 <= nx < 12 and 0 <= ny < 6): continue
            if visited[nx][ny] == 1: continue

            if graph[nx][ny] == puyo:
                q.append([nx, ny])
                visited[nx][ny] = 1 # 방문처리
                candidate_list.append([nx, ny])

    if len(candidate_list) >= 4: 
        for x, y in candidate_list:
            graph[x][y] = '.'

    return

# 뿌요 떨어뜨리기
def fall_puyo():
    for y in range(6):
        puyo_list = []
        for x in range(12):
            if graph[x][y] != '.':
                puyo_list.append(graph[x][y])
        
        no_puyo = 12 - len(puyo_list)
        yes_puyo = len(puyo_list)

        for i in range(no_puyo):
            graph[i][y] = '.'
        
        index = 0
        for i in range(no_puyo, 12):
            graph[i][y] = puyo_list[index]
            index += 1
            



    return

def is_break_ok():
    visited = [[0 for i in range(6)] for i in range(12)]
    

    for i in range(12):
        for j in range(6):
            if graph[i][j] == '.': continue 
            if visited[i][j] == 1: continue

            if not bfs(i, j, visited):
                return False


    return True

def bfs(x, y, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1 # 방문 처리
    puyo = graph[x][y]
    
    count = 1
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if not ( 0 <= nx < 12 and 0 <= ny < 6): continue
            if visited[nx][ny] == 1: continue

            if graph[nx][ny] == puyo:
                q.append([nx, ny])
                visited[nx][ny] = 1 # 방문처리
                count += 1

    if count >= 4: 
        return False 

    return True

while True:
    if is_break_ok():
        print(answer)
        break

    check_puyo_bfs()

    fall_puyo()

    answer += 1