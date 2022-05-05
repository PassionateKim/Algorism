#DFS 와 BFS
import sys
from collections import deque

# 입력
N, M, V = map(int,sys.stdin.readline().rstrip().split())
# 초기화
answer = []
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
# graph 에 간선 연결관계 넣기 
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 간선관계 정렬해주기
for i in graph:
    i.sort()


def dfs(value, depth):
    answer.append(value) # 값넣기
    visited[value] = 1 #  방문처리

    for i in graph[value]:
        if visited[i] == 0: # 방문하지 않았던 경우에만
            dfs(i, depth+1)
    return

def bfs(value):
    q = deque()
    q.append(value)
    answer.append(value)
    visited[value] = 1 # 방문처리

    while q:
        value = q.popleft()
        for i in graph[value]:
            if visited[i] == 0: # 방문하지 않았던 경우에만
                q.append(i)
                answer.append(i)
                visited[i] = 1 # 방문처리





dfs(V,0)
print(*answer)
answer = [] # 값 초기화
visited = [0] * (N+1)
bfs(V)
print(*answer)




# def dfs(n):
#     print(n)
#     visited[n] = True
#     for i in graph[n]:
#         if not visited[i]:
#             dfs(i)


# #node, branch, first node
# n,m,v = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n + 1)

# for _ in range(m):
#     a,b = map(int,sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
    

# for i in range(1, n+1):
#     graph[i].sort()

# print(graph)

# dfs(v)
