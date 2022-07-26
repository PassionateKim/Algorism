# N과 M(5)
import sys
si = sys.stdin.readline

N, M = map(int, si().split())
tmp = sorted(list(map(int, si().split())))

A = []

def dfs(idx):
    # 탈출조건
    if len(A) == M:
        print(*A)
        return 

    for i in range(len(tmp)):
        if tmp[i] not in A:
            A.append(tmp[i])
            dfs(i+1)
            A.pop()

    return

dfs(0)