# 탑
import sys
si = sys.stdin.readline

N = int(si())
top_list = list(map(int, si().split()))

stack = []
answer = []

for i in range(len(top_list)):
    while stack:
        if stack[-1][-1] < top_list[i]:# 6 < 9
            stack.pop()
        else:
            answer.append(stack[-1][0]+1)
            break

    if len(stack) == 0:
        answer.append(0)

    stack.append((i, top_list[i]))

print(*answer)