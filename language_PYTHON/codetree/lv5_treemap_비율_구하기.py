# 복습 횟수:0, 00:15:00, 복습필요X
import sys
from sortedcontainers import SortedDict

si = sys.stdin.readline
N = int(si())
mydict = SortedDict()

for i in range(N):
    inp = si().strip()
    if inp not in mydict.keys():
        mydict[inp] = 1
    else:
        mydict[inp] += 1

divider = sum(mydict.values())

for key, value in mydict.items():
    ratio = value / divider * 100
    print(f"{key} {ratio:.4f}")