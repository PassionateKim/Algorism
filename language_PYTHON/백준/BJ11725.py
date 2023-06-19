# 트리의 부모 찾기
# 복습 횟수:1, 00:30:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline
N = int(si())


graph = [[] for i in range(N+1)]
answer = [0] * (N+1)
visited = [0] * (N+1)

for i in range(N-1):
    x, y = map(int, si().split())
    graph[x].append(y)
    graph[y].append(x)


                 
def bfs(start):
    q = deque()
    visited[start] = 1 # 방문처리
    q.append(start)

    while q:
        idx = q.popleft()

        for val in graph[idx]:
            if visited[val]: continue

            q.append(val)
            answer[val] = idx
            visited[val] = 1

    return

bfs(1)

for i in range(2, len(answer)):
    print(answer[i])

