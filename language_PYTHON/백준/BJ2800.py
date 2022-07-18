# 괄호 제거
from itertools import combinations
import sys

si = sys.stdin.readline

l = [] # 안에서 밖 순서로 괄호 쌍의 위치를 저장한다.
stack = []
answer = set()
input = si().strip()
for idx, v in enumerate(list(input)):
    if v == '(':
        stack.append(idx)
    elif v == ')':
        start = stack.pop()
        end = idx
        l.append([start, end])

for i in range(1, len(l) + 1):
    combi = combinations(l, i)
    for j in combi:
        tmp = list(input)
        for k in j:
            start, end = k
            tmp[start] = ''
            tmp[end] = ''
        answer.add(''.join(tmp))

for i in sorted(list(answer)):
    print(i)
        
