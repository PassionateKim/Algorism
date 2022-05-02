# 큐
from collections import deque
import sys
from tkinter import E
input = sys.stdin.readline

N = int(input())
q = deque()
for i in range(N):
    c = input().rstrip()

    if "push" in c:
        q.append(c.split()[1])
    elif "pop" in c:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif "size" in c:
        print(len(q))
    elif "empty" in c:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif "front" in c:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif "back" in c:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])

