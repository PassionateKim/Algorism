#제로

import sys
from collections import deque

K = int(input())

queue = deque()

for i in range(K):
    input = int(sys.stdin.readline().rstrip())

    if(input == 0):
        if len(queue) != 0:
            queue.popleft()
            
    else:
        queue.appendleft(input)
    
answer = 0
for i in queue:
    answer += i

print(answer)

