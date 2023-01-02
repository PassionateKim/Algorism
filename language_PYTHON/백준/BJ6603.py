# 로또
import sys
si = sys.stdin.readline
answer = []

def dfs(count, idx):
    if count == 6:
        print(*answer)
    
    for i in range(idx, len(tmp)):
        answer.append(tmp[i])
        dfs(count + 1, i + 1)
        answer.pop()
        
while True:
    tmp = list(map(int, si().split()))
    if (tmp[0] == 0):
        break

    tmp = tmp[1:]
    dfs(0, 0)
    print()