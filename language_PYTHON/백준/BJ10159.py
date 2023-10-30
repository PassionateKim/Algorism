# 복습 횟수:0, 01:30:00, 복습필요O
import sys
si = sys.stdin.readline 
from collections import deque

N = int(si())
M = int(si())

# 1 > 2, 2 < 3 인 경우 - 예측 불가능

# 1 > 2, 2 > 3 인 경우 - 예측 가능

# 1 < 2, 2 < 3 인 경우 - 예측 가능

# 1 < 2, 2 > 3 인 경우 - 예측 불가능 

# graph에 누가 더 큰지를 체크하도록?? .. . 
# graph에 누가더 작은지를 체크 하도록

# bfs_high
# bfs_low 
# 두개 돌리고 set에 저장

graph_high = [[] for i in range(N+1)]
graph_low = [[] for i in range(N+1)]

def bfs_high(start, tmp_set: set):
    visited = [0 for i in range(N+1)]

    q = deque()
    q.append(start)
    visited[start] = 1 # 방문 처리 

    while q:
        start = q.popleft()
        
        for val in graph_high[start]:
            if visited[val] == 1: continue

            q.append(val)
            tmp_set.add(val)
            visited[val] = 1 # 방문처리
    return

def bfs_low(start, tmp_set: set):
    visited = [0 for i in range(N+1)]

    q = deque()
    q.append(start)
    visited[start] = 1 # 방문처리

    while q:
        start = q.popleft()

        for val in graph_low[start]:
            if visited[val] == 1: continue

            q.append(val)
            tmp_set.add(val)
            
            visited[val] = 1 # 방문처리

    return

for i in range(M):
    x, y = map(int, si().split())

    graph_high[x].append(y)
    graph_low[y].append(x)

for start in range(1, N+1):
    tmp_set = set()
    
    bfs_high(start, tmp_set)
    bfs_low(start, tmp_set)

    print(N-1 - len(tmp_set))