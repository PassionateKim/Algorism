import sys
si = sys.stdin.readline
myDict = dict()

N = int(si())
for i in range(N):
    val = si().rstrip()
    if val not in myDict.keys():
        myDict[val] = 1
    else:
        myDict[val] += 1

print(max(myDict.values()))