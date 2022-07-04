# 미세먼지 안녕!
import sys
from collections import deque
si = sys.stdin.readline

# 실수 유형 체크 
R, C, T = map(int, si().split())
cleaner = []
graph = []
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 그래프 초기화
for i in range(R):
    graph.append(list(map(int, si().split())))
    
# 청정기 위치 #으로 바꾸기 -> 중복때문
for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            graph[i][j] = '#'

for _ in range(T): # 탐색 시작
    # for 문으로 완탐 -> 청정기 위치, 미세먼지 위치
    # tmp graph 영향을 주면 안됨
    tmp_graph = [[0 for _ in range(C)] for __ in range(R)]
    dust_list = [] #  아 초기화를 안해줬네..
    
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '#': #청청기 위치
                cleaner.append((i,j))
            elif graph[i][j] != 0: 
                dust_list.append((i,j))
    
    # for 문으로 미세먼지 확산시키기
    for i in dust_list:
        x, y = i[0], i[1]
        if x == 5 and y == 7:
            pass
        tmp = graph[x][y] # 먼지량
        cnt = 0
        for idx in range(4): # 상하좌우
            nx, ny = x + dx[idx], y + dy[idx]
            if not (0<=nx<R and 0<=ny<C): continue # 범위 밖 X
            if graph[nx][ny] == '#': continue # 공기청정기 X 
            
            tmp_graph[nx][ny] += tmp // 5 # spread amount
            cnt += 1
        # 확산이 아예 안되는 경우는 없으므로 cnt == 0 체크하지 않음
        tmp_graph[x][y] -= (tmp//5) * cnt 


    # graph 수정하기
    for i in range(R):
        for j in range(C):
            if graph[i][j] != '#':
                graph[i][j] += tmp_graph[i][j]
                

    # 공기청정기로 옆으로 옮기기: q사용

    # 아래쪽
    q = deque()
    x, y = cleaner.pop()
    
    # 오른쪽으로 쭉 이동
    tmp_x, tmp_y = x, y+1
    while y < C-1:
        y += 1 # 이동
        
        q.append(graph[x][y]) # 2
        
        if len(q) > 1: # q = [5,2]
            tmp = q.popleft() # 5
            graph[x][y] = tmp # 5로 변경 -> [2]
    # 기존 제거
    graph[tmp_x][tmp_y] = 0
    
    
    # 아래로 쭉 이동
    while x < R-1:
        x += 1
        q.append(graph[x][y]) # 2
        
        if len(q) > 1: # q = [5,2]
            tmp = q.popleft() # 5
            graph[x][y] = tmp # 5로 변경 -> [2]
    
    # 왼쪽으로 쭉 이동
    while y > 0:
        y -= 1
        q.append(graph[x][y]) # 2
        
        if len(q) > 1: # q = [5,2]
            tmp = q.popleft() # 5
            graph[x][y] = tmp # 5로 변경 -> [2]
    
    # 에어컨까지 위로 이동
    while x > tmp_x+1:
        x -= 1
        q.append(graph[x][y]) # 2
        
        if len(q) > 1: # q = [5,2]
            tmp = q.popleft() # 5
            graph[x][y] = tmp # 5로 변경 -> [2]
    
    # 위쪽
    q = deque()
    x, y = cleaner.pop()
    tmp_x, tmp_y = x, y+1

    # 오른쪽으로 쭉 이동
    while y < C-1:
        y += 1 # 이동
        q.append(graph[x][y]) # 2
        
        if len(q) > 1: # q = [5,2]
            tmp = q.popleft() # 5
            graph[x][y] = tmp # 5로 변경 -> [2]
    
    graph[tmp_x][tmp_y] = 0 # 기존 제거

    # 위로 이동
    while x > 0:
        x -= 1
        q.append(graph[x][y]) # 2
        
        if len(q) > 1: # q = [5,2]
            tmp = q.popleft() # 5
            graph[x][y] = tmp # 5로 변경 -> [2]

    # 왼쪽으로 쭉 이동
    while y > 0:
        y -= 1
        q.append(graph[x][y]) # 2
        
        if len(q) > 1: # q = [5,2]
            tmp = q.popleft() # 5
            graph[x][y] = tmp # 5로 변경 -> [2]
    
    # 아래로 쭉 이동
    while x < tmp_x-1:
        x += 1
        q.append(graph[x][y]) # 2
        
        if len(q) > 1: # q = [5,2]
            tmp = q.popleft() # 5
            graph[x][y] = tmp # 5로 변경 -> [2]
  
# 총 계산
answer = 0 
for i in range(R):
    for j in range(C):
        if graph[i][j] == '#': continue
        
        answer += graph[i][j]
print(answer)
