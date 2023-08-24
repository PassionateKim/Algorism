# 외판원 순회 2
# 복습 횟수:1, 00:45:00, 복습필요X
import sys
si = sys.stdin.readline 
N = int(si())

graph = []
for i in range(N):
    tmp = list(map(int, si().split()))
    graph.append(tmp)

visited = [0 for i in range(N)]
answer = sys.maxsize

def dfs(sumi, current):
    global answer

    if visited.count(0) == 0: # 모두 돌았을 때
        if graph[current][start]:
            sumi = sumi + graph[current][start]
            answer = min(answer, sumi)
        return

    for index, next in enumerate(graph[current]):
        if visited[index] == 1: continue
        if next == 0: continue

        visited[index] = 1 
        dfs(sumi + graph[current][index], index)
        visited[index] = 0

    return

for start in range(N):
    visited[start] = 1 # 방문처리
    dfs(0, start)
    visited[start] = 0 # 초기화

print(answer)