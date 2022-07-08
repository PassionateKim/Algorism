# 부분수열의 합
import sys
si = sys.stdin.readline

N, S = map(int, si().split())
A = list(map(int, si().split()))

answer = 0

def dfs(depth, sum):
    global answer
    if depth == N:
        return

    sum += A[depth]

    if sum == S:
        answer += 1

    # dfs
    dfs(depth+1, sum)
    dfs(depth+1, sum - A[depth])
    
    return

dfs(0, 0)
print(answer)