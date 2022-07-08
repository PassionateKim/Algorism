#회전하는 큐
import sys
from collections import deque
si = sys.stdin.readline
N, M = map(int, si().split())

sequence = deque(map(int, si().split()))
q = deque([i for i in range(1, N+1)])

cnt = 0

for s in sequence:
    if s == q[0]:
        q.popleft()
    else:
        if q.index(s) <= len(q) // 2:
            while True: # 왼쪽에 있는 걸 오른쪽으로 
                q.append(q.popleft())
                cnt += 1 
                if s == q[0]:
                    q.popleft()
                    break
        else:
            while True: # 오른쪽에 있는 걸 왼쪽으로
                q.appendleft(q.pop())
                cnt += 1
                if s == q[0]:
                    q.popleft()
                    break
    
print(cnt)