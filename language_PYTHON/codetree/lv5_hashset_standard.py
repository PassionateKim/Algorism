# 복습 횟수:0, 00:10:00, 복습필요X
import sys
si = sys.stdin.readline

myset = set()
N = int(si())
for i in range(N):
    cmd_list = si().rstrip().split()
    if "find" in cmd_list:
        cmd, k = cmd_list
        if k in myset:
            print("true")
        else:
            print("false")
    
    if "add" in cmd_list:
        cmd, k = cmd_list
        myset.add(k)
    
    if "remove" in cmd_list:
        cmd, k = cmd_list
        if k in myset:
            myset.remove(k)
        else: pass