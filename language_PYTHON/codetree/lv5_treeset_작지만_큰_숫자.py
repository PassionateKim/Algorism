# 복습 횟수:0, 01:00:00, 복습필요X
from sortedcontainers import SortedSet
import sys
si = sys.stdin.readline
N, T = map(int, si().split())

tmp_list = list(map(int, si().split()))
mySet = SortedSet()

for val in tmp_list:
    mySet.add(val)

input_list = list(map(int, si().split()))

def check(input):
    index = mySet.bisect_right(input)
    return index - 1

for input in input_list:
    index = check(input)

    if (index == -1):
        print(-1)
    else:
        print(mySet[index])
        if(len(mySet) != 0):
            mySet.remove(mySet[index])