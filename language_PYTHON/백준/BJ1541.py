import sys
si = sys.stdin.readline

li = list(map(str, si().rstrip().split("-")))
answer = 0

if '+' in li[0]:
    tmp = list(map(int, li[0].split('+')))
    answer = sum(tmp)
else:
    answer = int(li[0])

for i in range(1, len(li)):
    if '+' in li[i]:
        tmp = list(map(int, li[i].split('+')))
        answer = answer - sum(tmp)
    else:
        answer = answer - int(li[i])

print(answer)