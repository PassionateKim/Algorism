# 로또
from itertools import combinations

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    
    for i in range(start, len(set_S)):
        combi[depth] = set_S[i]
        dfs(i + 1, depth + 1)

combi = [0 for i in range(13)]

while True:
    # 입력
    set_S = list(map(int, input().split()))
    
    if set_S[0] == 0:
        break

    del set_S[0]
    dfs(0,0)
    print()
