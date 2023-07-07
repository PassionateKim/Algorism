from sortedcontainers import SortedDict
import sys
si = sys.stdin.readline

N = int(si())
mydict = SortedDict()

for i in range(N):
    inp = si().strip()
    if inp not in mydict.keys():
        mydict[inp] = 1
    else:
        mydict[inp] += 1


for key, value in mydict.items():
    print(key, value)