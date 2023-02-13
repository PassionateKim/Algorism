# 줄어드는 수
# 복습 횟수:1, 00:45:00
import sys
sys.setrecursionlimit(10**6)
si = sys.stdin.readline
N = int(si())
answer = 0

def dfs(count, idx, number: list):
    if count == idx:
        global answer
        answer += 1
        if answer == N:
            print(int("".join(number)))
            exit()
        return
    
    for i in range(10):
        if len(number) == 0:
            number.append(str(i))
            dfs(count, idx + 1, number)
            number.pop()
        elif int(number[-1]) > i :
            number.append(str(i))
            dfs(count, idx + 1, number)
            number.pop()
    return

for i in range(1, 11):
    dfs(i, 0, [])

if N > answer:
    print(-1)