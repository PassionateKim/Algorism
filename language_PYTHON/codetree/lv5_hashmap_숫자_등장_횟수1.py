import sys
si = sys.stdin.readline
dic = dict()
N, M = map(int, si().split())
li = list(map(int, si().split()))
for val in li:
    if(val not in dic.keys()):
        dic[val] = 1
    else:
        dic[val] += 1

check_nums = list(map(int, si().split()))
for num in check_nums:
    if(num in dic.keys()):
        print(dic[num], end=' ')
    else:
        print(0, end=' ')