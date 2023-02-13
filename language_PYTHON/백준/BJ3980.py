# 선발 명단
# 복습 횟수:1, 00:30:00, 복습 필요X
import sys
si = sys.stdin.readline
N = int(si())

def dfs(current):
    global answer
    if current == 11:
        sumi = 0
        for location, val in visited:
            sumi += val
        answer = max(answer, sumi)
        return

    for i in range(11):
        if visited[i] == 0 and graph[current][i] != 0:
            visited[i] = [current, graph[current][i]]
            dfs(current + 1)
            visited[i] = 0 # 초기화

    return

for i in range(N):
    answer = 0
    graph = [list(map(int, si().split())) for _ in range(11)]
    visited = [0 for _ in range(11)]

    dfs(0)
    print(answer)