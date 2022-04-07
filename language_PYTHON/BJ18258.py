#큐2
import sys
from collections import deque
queue = deque()

N = int(input())

for i in range(N):
    char = sys.stdin.readline().rstrip()
    
    if "push" in char:
        a = list(map(str,char.split()))
        queue.append(a[1])
    elif "pop" == char:
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue.popleft())
    elif "size" == char:
        print(len(queue))
    elif "empty" == char:
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
    elif "front" == char:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif "back" == char:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])


