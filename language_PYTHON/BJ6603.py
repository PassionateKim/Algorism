# 로또
from itertools import combinations

while True:
    # 입력
    set_S = list(map(int, input().split()))
    
    if set_S[0] == 0:
        break

    del set_S[0]
    s = list(combinations(set_S, 6))
    
    for i in s:
        print(*i)
    print()
