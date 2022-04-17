#덱
from collections import deque

d = deque()
N = int(input())
for i in range(N):
    a = input()
    if "push_front" in a:
        d.appendleft(a.split()[1])
    elif "push_back" in a:
        d.append(a.split()[1])
    elif "pop_front" in a:
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif "pop_back" in a:
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif "size" in a:
        print(len(d))
    elif "empty" in a:
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif "front" in a:
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif "back" in a:
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])        
    
