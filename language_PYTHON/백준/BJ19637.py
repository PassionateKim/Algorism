# if문 좀 대신 써줘
# 복습 횟수:0, 00:30:00, 복습필요:X
import sys
from collections import defaultdict
si = sys.stdin.readline
N, M = map(int, si().split())
title_list = []
title_dict = defaultdict(str)
c_list = []

for i in range(N):
    title = list(map(str, si().split()))
    title_list.append(title)
for j in range(M):
    c = int(si())
    c_list.append(c)

title_list.reverse()
for a, b in title_list:
    title_dict[b] = a

title_list = []

for key, value in title_dict.items():
    title_list.append([value, int(key)])

title_list.sort(key=lambda x: x[1])

def binary(start, end, target):
    tmp = '$'
    while start <= end:
        idx = (start + end) // 2
        mid = title_list[idx][1]

        if mid >= target:
            tmp = title_list[idx][0]
            end = idx - 1
        else:
            start = idx + 1
    answer.append(tmp)        
    return

answer = []
for c in c_list:
    binary(0, len(title_list) - 1, c)

for a in answer:
    print(a)