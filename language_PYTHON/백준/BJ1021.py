#회전하는 큐
# 복습 횟수:2,00:30:00, 복습필요O
import sys
from collections import deque
si = sys.stdin.readline
N, M = map(int, si().split())
double_q = deque ()

for i in range(1, N + 1):
    double_q.append(i)

li = list(map(int, si().split()))
answer = 0
for val in li:
    if double_q[0] == val:
        double_q.popleft()
    else:
        left = double_q.index(val)
        right = len(double_q) - left
        if left <= right:
            while True:
                if double_q[0] == val:
                    double_q.popleft()
                    break
                tmp = double_q.popleft()
                double_q.append(tmp)
                answer += 1
        else: # left > right:
            while True:
                if double_q[0] == val:
                    double_q.popleft()
                    break
                tmp = double_q.pop()
                double_q.appendleft(tmp)
                answer += 1

print(answer)