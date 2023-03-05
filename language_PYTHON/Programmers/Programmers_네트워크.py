# 복습 횟수:0, 00:30:00, 복습필요X
from collections import deque
def bfs(start, check):
    q = deque()
    q.append(start)
    visited[start] = check
    
    while q:
        idx = q.popleft()
        for val in graph[idx]:
            if visited[val] == 0:
                q.append(val)
                visited[val] = check
    
    return

def solution(n, computers):
    global visited
    global graph
    answer = 0
    graph = [[] for i in range(n)]

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if (computers[i][j] == 1):
                graph[i].append(j)
    visited = [0 for i in range(n)]
    
    check = 1
    for idx in range(len(graph)):
        if visited[idx] == 0:
            bfs(idx, check)
            check += 1
    answer = max(visited)
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
