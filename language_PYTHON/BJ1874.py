#스택 수열
import sys
stack = []
answer = []
cur = 1
flag = 0
n = int(input())
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1

    if(stack[-1] == num):
        stack.pop()
        answer.append('-')
    else:
        flag = 1


if flag == 0:
    for i in answer:
        print(i)
else:
    print("NO")

