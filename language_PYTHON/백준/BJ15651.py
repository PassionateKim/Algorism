# N과 M(3)
import sys
si = sys.stdin.readline

N, M = map(int, si().split())

answer = []
visited = [0 for i in range(N+1)]

def dfs(count):

    if (count == M):
        print(*answer)
        return

    for i in range(1, N + 1):
        answer.append(i)
        dfs(count+1)
        answer.pop()

dfs(0)