# 도영이가 만든 맛있는 음식
# 복습 횟수:0, 00:30:00, 복습필요X
import sys
from itertools import combinations
si = sys.stdin.readline
N = int(si())
answer = sys.maxsize

ingredient_list = []
for i in range(N):
    ingredient = list(map(int, si().split()))
    ingredient_list.append(ingredient)


for i in range(1, N+1):
    combi_list = list(combinations(ingredient_list, i))
    for combi in combi_list:
        S = 1
        B = 0
        for s, b in combi:
            S = S * s
            B = B + b
        tmp = abs(S-B)
        answer = min(answer, tmp)
print(answer)