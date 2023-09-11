import sys
from collections import deque
si = sys.stdin.readline 
N, P = map(int, si().split())



def bfs():
    q = deque()
    q.append(N)
    visited = [0 for _ in range(1000000 + 1)]
    visited[N] += 1 # 방문처리

    while q:
        val = q.popleft()
        val = str(val)
        if val == 3:
            break

        number_list_str = list(val)
        new_val = 0
        for number_str in number_list_str:
            new_val = new_val + pow(int(number_str), P) 
        
        if visited[new_val] <= 2:
            q.append(new_val)
            visited[new_val] += 1 

    print(visited.count(1))
    return
bfs()