# 2023-07-15
# 2023-07-23
# 복습 횟수:2, 00:30:00, 복습필요:***
import sys
si = sys.stdin.readline

N, K = map(int, si().split())
elem_list = list(map(int, si().split()))

mydict = dict()
answer = 0
for elem in elem_list:
    if elem not in mydict:
        mydict[elem] = 1
    else:
        mydict[elem] += 1

for i in range(len(elem_list)):
    mydict[elem_list[i]] -= 1

    for j in range(i):
        diff = K - elem_list[i] - elem_list[j]
        
        if diff in mydict.keys():
            answer += mydict[diff]

print(answer)