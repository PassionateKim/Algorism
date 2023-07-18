import heapq
import sys
si = sys.stdin.readline
myque = list()

N = int(si())

for i in range(N):
    cmd_list = list(map(str, si().rstrip().split()))

    if "push" in cmd_list:
        cmd, num = cmd_list
        num = int(num)

        heapq.heappush(myque, tuple([-num, num]))
    
    if "size" in cmd_list:
        print(len(myque))
    
    if "empty" in cmd_list:
        if len(myque) == 0:
            print(1)
        else:
            print(0)
    
    if "pop" in cmd_list:
        print(myque[0][1])
        heapq.heappop(myque)
    
    if "top" in cmd_list:
        print(myque[0][1])