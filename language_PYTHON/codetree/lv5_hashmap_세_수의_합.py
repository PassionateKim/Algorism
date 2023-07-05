# 복습 횟수:0, 01:30:00, 복습필요O

import sys
si = sys.stdin.readline

N, K = map(int, si().split())
arr = list(map(int, si().split()))

mydict = dict()

for i in range(len(arr)):
    if( arr[i] not in mydict.keys()):
        mydict[arr[i]] = 1
    else:
        mydict[arr[i]] += 1
answer = 0

for i in range(len(arr)):

    mydict[arr[i]] -= 1

    for j in range(i):
        diff = K - arr[i] - arr[j]

        if(diff in mydict.keys()):
            answer += mydict[diff]

print(answer)
