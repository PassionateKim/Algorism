# N-Queen
# 복습 횟수:3, 01:00:00, 복습필요X
import sys
si = sys.stdin.readline 
N = int(si())
answer = 0

n_queen = [0 for i in range(N+1)]

def is_promising(depth, x):
    
    # 가로 체크 ( 세로는 이미 체크한 상태이다. )
    for row in range(1, depth):
        if n_queen[row] == x or (abs(n_queen[row] - x) == abs(row - depth)):
            return False
    
    return True

def dfs(depth):
    global answer

    if depth == N + 1:
        answer += 1
        return
    
    for i in range(1, N + 1):
        n_queen[depth] = i

        if is_promising(depth, i):
            dfs(depth + 1)

    return

dfs(1)
print(answer)