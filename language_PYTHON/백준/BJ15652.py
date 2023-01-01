# N과 M(4)
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
answer = []

def dfs(count, idx):

    if (count == M):
        print(*answer)
        return
    
    for i in range(idx, N+1):
        answer.append(i)
        dfs(count+1, i)
        answer.pop()

dfs(0, 1)