# 2023-07-13
# 복습 횟수:1, 00:20:00, 복습필요X
import sys
si = sys.stdin.readline
N = int(si())

mydict = dict()
for i in range(N):
    input = list(map(str, si().rstrip()))
    key = "".join(sorted(input))
    
    if key not in mydict.keys():
        mydict[key] = 1
    else:
        mydict[key] += 1

print(max(mydict.values()))