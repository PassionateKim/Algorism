import sys
from collections import defaultdict
si = sys.stdin.readline 
dot_dict = defaultdict(list)

answer = 0
N = int(si())
for i in range(N):
    location, color = map(int, si().split())
    dot_dict[color].append(location)

for key, value in dot_dict.items():
    value.sort()

for key in dot_dict.keys():
    for i, value in enumerate(dot_dict[key]):
        if i == 0:
            diff = dot_dict[key][1] - dot_dict[key][0]
            answer = answer + diff
        elif i == len(dot_dict[key]) - 1:
            diff = dot_dict[key][-1] - dot_dict[key][-2]
            answer = answer + diff 
        else:
            less = min(abs(dot_dict[key][i] - dot_dict[key][i+1]), abs(dot_dict[key][i] - dot_dict[key][i-1]))
            answer = answer + less

print(answer)