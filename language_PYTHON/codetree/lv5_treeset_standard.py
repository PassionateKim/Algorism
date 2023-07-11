# 복습 횟수:0, 00:10:00, 복습필요X
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline

N = int(si())
myTreeSet = SortedSet()

for i in range(N):
    cmd_list = list(map(str, si().rstrip().split()))
    if "add" in cmd_list:
        cmd, k = cmd_list
        myTreeSet.add(int(k))
    
    if "remove" in cmd_list:
        cmd, k = cmd_list
        myTreeSet.remove(int(k))
    
    if "find" in cmd_list:
        cmd, k = cmd_list
        if int(k) in myTreeSet:
            print("true")
        else:
            print("false")
    
    if "lower_bound" in cmd_list:
        cmd, k = cmd_list
        index = myTreeSet.bisect_left(int(k))
        if (index == len(myTreeSet)):
            print("None")
        else:
            print(myTreeSet[index])

    if "upper_bound" in cmd_list:
        cmd, k = cmd_list
        index = myTreeSet.bisect_right(int(k))
        if(index == len(myTreeSet)):
            print("None")
        else:
            print(myTreeSet[index]) 

    if "largest" in cmd_list:
        if (len(myTreeSet) == 0):
            print("None")
        else:
            print(myTreeSet[-1])

    if "smallest" in cmd_list:
        if (len(myTreeSet) == 0):
            print("None")
        else:
            print(myTreeSet[0])