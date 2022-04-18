#회전하는 큐
from collections import deque
import sys

N,M = map(int,input().split())

dq = deque(i for i in range(1,N+1))
idxs = list(map(int,input().split()))

def left(m):
    m.append(m.popleft())
    
def right(m):
    m.appendleft(m.pop())

cnt = 0
for i in range(M):
    while True:
        
        if dq[0] == idxs[0]:
            # print("pop!")
            idxs.pop(0)
            dq.popleft()
            break
        else:
            if dq.index(idxs[0]) < len(dq) / 2:
                # print("left!")
                left(dq)
                cnt += 1
            else:
                # print("right!")
                right(dq)
                cnt += 1

print(cnt)

