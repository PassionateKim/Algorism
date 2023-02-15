# N-Queen
# 복습 횟수:1, 02:30:00, 복습필요O
import sys
si = sys.stdin.readline
N = int(si())

row = [0] * (N)
answer = 0

def isPromising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True

def dfs(index):
    global answer
    if index == N:
        answer += 1

    else:
        for i in range(N):
            row[index] = i
            if isPromising(index):
                dfs(index + 1)            

dfs(0)
print(answer)