# 스타트링크
# 복습 횟수:0, 00:30:00, 복습필요X
import sys
from collections import deque
si = sys.stdin.readline 
F, S, G, U, D = map(int, si().split())

def bfs():
    visited = [0 for i in range(F+1)]
    q = deque()
    q.append([S, 0])
    visited[S] = 1 # 방문처리

    while q:
        current, count = q.popleft()

        # 도착하면
        if (current == G):
            return count
        
        if(current + U <= F and visited[current + U] != 1):
            q.append([current + U, count + 1])
            visited[current + U] = 1 # 방문처리
        if(current - D >= 1 and visited[current - D] != 1):
            q.append([current - D, count + 1])
            visited[current - D] = 1 # 방문처리

    return -1
answer = bfs()
if(answer != -1):
    print(answer)
else:
    print("use the stairs")