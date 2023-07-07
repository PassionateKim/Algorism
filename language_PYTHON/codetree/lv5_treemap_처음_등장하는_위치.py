# 복습 횟수:0, 00:15:00, 복습필요X
from sortedcontainers import SortedDict
import sys
si = sys.stdin.readline

N = int(si())
arr_list = list(map(int, si().split()))

mydict = SortedDict()

for index, val in enumerate(arr_list):
    if val not in mydict:
        mydict[val] = index + 1

for key, value in mydict.items():
    print(key, value) 