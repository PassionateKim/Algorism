# 복습횟수:0, 00:30:00, 복습필요X
import sys
si = sys.stdin.readline
string_ = list(map(str, si().strip()))


mydict = dict()

for index, s in enumerate(string_):
    if s not in mydict.keys():
        mydict[s] = [1, index]
    else:
        mydict[s][0] += 1

candidate = []

for key, value in mydict.items():
    if value[0] == 1:
        candidate.append(value)

if len(candidate) == 0:
    print("None")
else:
    candidate.sort(key=lambda x: x[1])
    firstIndex = candidate[0][1]

    for key,value in mydict.items():
        if value[1] == firstIndex:
            print(key)
            break