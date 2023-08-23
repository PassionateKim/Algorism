# N-Queen
# 복습 횟수:2, 01:30:00, 복습필요1
import sys
si = sys.stdin.readline 
N = int(si())

visited = [0 for i in range(N)]
answer = 0

def isPromising(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == abs(x - i):
            return False
    
    return True

def dfs(depth):
    global answer

    if depth == N:
        answer += 1

    else:
        for i in range(N):
            visited[depth] = i
            if isPromising(depth):
                dfs(depth + 1)  

dfs(0)
print(answer)