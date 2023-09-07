# 복습 횟수:0, 02:30:00, 복습필요3
from collections import deque
import sys
si = sys.stdin.readline 
N, M = map(int, si().split())

graph = []
for i in range(N):
    tmp = list(map(str, si().rstrip()))
    graph.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
check = [0] * 26
def dfs(x, y, length):
    global answer 
    answer = max(answer, length)

    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]
        if (0 <= nx < N and 0 <= ny < M):

                string_val = graph[nx][ny]

                if check[ord(string_val) - 65] == 0: 
                    check[ord(string_val) - 65] = 1
                    dfs(nx, ny, length + 1)
                    check[ord(string_val) - 65] = 0

    return

check[ord(graph[0][0]) - 65] = 1 # 방문처리
dfs(0, 0, 1)
print(answer)