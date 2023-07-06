# 복습 횟수:0, 02:00:00, 복습필요O
import sys
si = sys.stdin.readline

N = int(si())
arr_list = []
for i in range(4):
    tmp = list(map(int, si().split()))
    arr_list.append(tmp)

mydict = dict()
answer = 0
for i in range(len(arr_list[0])):
    for j in range(len(arr_list[1])):
        sumi = arr_list[0][i] + arr_list[1][j]
        if(sumi not in mydict.keys()):
            mydict[sumi] = 1
        else:
            mydict[sumi] += 1


for i in range(len(arr_list[2])):
    for j in range(len(arr_list[3])):
        sumi = arr_list[2][i] + arr_list[3][j]
        diff = 0 - sumi
        if diff in mydict.keys():
            answer += mydict[diff]

print(answer)