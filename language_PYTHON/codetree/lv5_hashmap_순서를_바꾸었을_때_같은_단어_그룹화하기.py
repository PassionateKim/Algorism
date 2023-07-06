# 복습 횟수:0, 01:00:00, 복습필요O
import sys
si = sys.stdin.readline

N = int(si())
mydict = dict()
for i in range(N):
    string_ = list(map(str, si().rstrip()))
    sortedString = "".join(sorted(string_))
    if sortedString not in mydict.keys():
        mydict[sortedString] = 1
    else:
        mydict[sortedString] += 1

print(max(mydict.values()))