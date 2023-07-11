# 복습 횟수:0, 00:15:00, 복습필요X
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline

t = int(si())
for i in range(t):
    n = int(si())
    s = SortedSet()

    for _ in range(n):
        command, x = map(str, si().split())

        x = int(x)
        # tree set 에 넣기

        if command == 'I':
            s.add(x)
        elif command == 'D' and s:
            if x == 1:
                s.remove(s[-1])
            else:
                s.remove(s[0])
    
    if not s:
        print("EMPTY")
    else:
        print(s[-1], s[0])