# 복습 횟수:0, 00:15:00, 복습필요X
import sys
si = sys.stdin.readline
N = int(si())
mydict = dict()

for i in range(N):
    x, y = map(int, si().split())
    if x not in mydict.keys():
        mydict[x] = y
    else:
        if mydict[x] > y:
            mydict[x] = y

print(sum(mydict.values()))