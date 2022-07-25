# 괄호 제거
from itertools import combinations
import sys
si = sys.stdin.readline

input = si().rstrip()
stack = []
location_list = []
answer = set()
# 괄호 위치 및 쌍 구하기
for idx, str in enumerate(input):
    if str == '(':
        stack.append(['(', idx])
    elif str == ')':
        x, location = stack.pop()
        location_list.append([location, idx])


for i in range(1, len(location_list)+1):
    combis = list(combinations(location_list, i))

    for combi in combis: # ([3, 5], )
        tmp = list(input)
        for z in combi: # [3, 5]
            x, y = z
            tmp[x] = ''
            tmp[y] = ''
        answer.add("".join(tmp))

answer = sorted(list(answer))
for i in answer:
    print(i)