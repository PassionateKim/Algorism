# 택배
# 복습 횟수:0, 01:00:00, 복습필요O
from collections import defaultdict
from itertools import combinations
import sys
si = sys.stdin.readline

work_dict = defaultdict(list)
N, C = map(int, si().split())

M = int(si())
for i in range(M):
    from_, to_, amount_ = map(int, si().split()) 
    work_dict[from_].append([to_, amount_])

answer = 0

amount_list = []
for val in work_dict.values():

    for x, y in val:
        amount_list.append(y)

for i in range(1, len(amount_list) + 1):
    candidate_list = list(combinations(amount_list, i))
    for candidate in candidate_list:
        sumi = sum(candidate)
        if sumi > C: 
            answer = C
        else:
            answer = max(sumi, answer)

print(answer)