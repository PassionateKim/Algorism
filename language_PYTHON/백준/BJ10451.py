from collections import deque
import sys

si = sys.stdin.readline 

T = int(si())

def bfs(start):
    global answer
    q = deque()
    q.append(start)
    visited[start] = 1 # 방문처리

    while q:
        start_val = q.popleft()
        end_val = arr[start_val - 1]
        
        if end_val == start:
            answer += 1
            return
        
        q.append(end_val)
        visited[end_val] = 1

    return

for case_index in range(T):
    answer = 0
    N = int(si())
    visited = [0 for i in range(N+1)] # index 1부터 시작
    arr = list(map(int, si().split()))

    for start in arr:
        if visited[start] != 0: continue

        bfs(start)
    
    print(answer)