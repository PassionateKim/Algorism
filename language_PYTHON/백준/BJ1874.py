# 2022-08-06
# 스택 수열
import sys
si = sys.stdin.readline
N = int(si().strip())
answer = []
stack = []
for i in range(N):
    stack.append(int(si().strip()))
stack.reverse()
# push의 개수는 정해져 있다.
tmp = []
for i in range(1, N+1):
    tmp.append(i)
    answer.append('+')
    while stack and tmp[-1] == stack[-1]:
        tmp.pop()
        stack.pop()
        answer.append('-')
if stack:
    print("NO")
else:
    for i in answer:
        print(i)