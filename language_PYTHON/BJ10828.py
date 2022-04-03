#스택
import sys
from collections import deque
N = int(input())

queue = deque()

for i in range(N):
    input = sys.stdin.readline().rstrip()
    if "push" in input:
        b = input.split()[1]
        queue.append(b)
    elif input == "pop":
        if(len(queue) == 0):
            print(-1)
        else:
            v = queue.pop()
            print(v)
    elif input == "top":
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[-1])
    elif input == "size":
        print(len(queue))
    elif input == "empty":
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
