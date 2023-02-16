# 외판원 순회 2
# 복습 횟수:0, 00:45:00, 복습필요O
import sys
si = sys.stdin.readline
N = int(si())
graph = [list(map(int, si().split())) for i in range(N)]
visited = [0 for i in range(N)]
answer = sys.maxsize
def dfs(first, start, count, sumi):
    global answer
    if count == N-1: 
        if graph[start][first] == 0: return

        answer = min(answer, sumi + graph[start][first])
        
        return
    
    for i in range(N):
        if visited[i]: continue
        if graph[start][i] == 0: continue

        visited[i] = 1
        tmp = graph[start][i]
        dfs(first, i, count + 1, sumi + tmp)
        visited[i] = 0
    return

for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 0)
    visited[i] = 0

print(answer)