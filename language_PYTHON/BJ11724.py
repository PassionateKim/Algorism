# 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph =  [[] for _ in range(N+1)] # idx 1부터 시작하기 위해서
visited = [0] * (N+1) # 방문처리를 위한 list

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()



def dfs(idx):
    visited[idx] = 1 # 방문처리

    for i in graph[idx]:
        if visited[i] == 0:
            dfs(i)
    

cnt = 0
for i in range(1, len(graph)):
    if visited[i] == 0: # 방문하지 않은 경우만
        dfs(i)
        cnt += 1 # 연결 요소 추가
print(cnt)
