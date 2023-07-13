# 2023-07-13
# 복습 횟수:1, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline
N, K = map(int, si().split())
elem_list = list(map(int, si().split()))

mydict = dict()
for elem in elem_list:
    if elem not in mydict.keys():
        mydict[elem] = 1
    else:
        mydict[elem] += 1

sortedDict = sorted(mydict.items(), key=lambda x: [-x[1], -x[0]])

for i in range(K):
    print(sortedDict[i][0], end = ' ')
