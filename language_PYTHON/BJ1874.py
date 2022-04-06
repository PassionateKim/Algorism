#스택 수열
import sys
stack = []
answer = []

n = int(input())
cnt = 1
flag = 0
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    while cnt <= a:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    print(cnt,stack)
    if stack[-1] == a:
        stack.pop()
        answer.append('-')
    else:
        flag = 1

if flag == 0:
    for i in answer:
        print(i)