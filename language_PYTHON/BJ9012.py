#괄호
from collections import deque
import sys
T = int(input())

def VPS(char):
    for i in char:
        if("(" == i):
            q.append(i)
        else:
            if(len(q) == 0):
                print("NO")
                return
            else:
                q.pop()
    if not len(q) == 0:
        print("NO")
    else:
        print("YES")        


for i in range(T):
    char_list = list(map(str,sys.stdin.readline().rstrip()))
    q =deque()
    VPS(char_list)
    


    
