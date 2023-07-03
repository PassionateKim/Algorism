import sys
si = sys.stdin.readline
N, M = map(int, si().split())
num_list = list(map(int, si().split()))

myDict = dict()
answer = 0

for num in num_list:
    if M-num in myDict:
        answer += myDict[M-num]
    
    if num in myDict:
        myDict[num] += 1
    else:
        myDict[num] = 1

print(answer)