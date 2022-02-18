#블랙잭

#입력 첫째 줄
N,M = map(int,input().split())

#입력 둘째 줄
cards = list(map(int,input().split()))

sums =set()

for i in cards:
    for j in cards:
        if j == i:
           continue
        for k in cards:
            if k == i or k == j:
                continue
            sums.add(i + j + k)
sums = list(sums)
sums.sort()

result = 0
for i in range(len(sums)):
    if(sums[i] <= M and sums[i] > result):
        result = sums[i]
    else:
        continue

print(result)
