# 여행가자
# 복습 횟수:0, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline

N = int(si())
M = int(si())

graph = [[] for _ in range(N+1)]
# graph 초기화
for i in range(N):
    tmp = list(map(int, si().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            graph[i+1].append(j+1)

answer = "YES"

def dfs(start, end):
    visited[start] = 1 # 방문 처리
    # 탈출 조건
    if start == end:
        return True
    
    for val in graph[start]:
        if visited[val] == 1: continue

        if dfs(val, end):
            return True

    return False

root = list(map(int, si().split()))
for i in range(len(root)-1):
    visited = [0 for _ in range(N+1)]
    if not dfs(root[i], root[i+1]):
        answer = "NO"

print(answer)    