# 듣보잡 
import sys
si = sys.stdin.readline

N, M = map(int, si().split())
listen, see = [], []
answer = []
cnt = 0
for i in range(N):
    listen.append(si().strip())

for j in range(M):
    see.append(si().strip())

listen.sort()


def Binary(array, start, end, target):
    global cnt
    while start<=end:
        mid = (start+end)//2

        if array[mid] == target:
            answer.append(array[mid])
            return
        
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0






for s in see:
    Binary(listen, 0, len(listen)-1, s)

print(len(answer))
answer.sort()
for i in answer:
    print(answer)