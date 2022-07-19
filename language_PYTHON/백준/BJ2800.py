# 괄호 제거
from itertools import combinations
import sys
si = sys.stdin.readline

input = si().strip()
stack = []
candidate = []
answer = list()

# 쌍 저장하기
for idx, str in enumerate(input):
    if str == '(':
        stack.append([idx, str])
    elif str == ')':
        i, s = stack.pop()
        candidate.append([i, idx])

# combination으로 문제 해결하기
for i in range(1, len(candidate) + 1):
    combi = combinations(candidate, i) #(([3, 6], [0, 5]), ([3, 6], [1, 7]), ([0, 5], [1,7])) 
    for l in combi: # ([3, 6], [0, 5])   ([3, 6], [1, 7])   ([0, 5], [1,7])
        tmp = list(input) 
        for k in l: 
            left, right = k
            tmp[left] = ''
            tmp[right] = ''
        answer.append("".join(tmp))

for i in sorted(answer):
    print(i)
