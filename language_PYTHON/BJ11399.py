#ATM

N = int(input())
times = list(map(int,input().split()))
times.sort()
part = 0
sum = 0

for i in times:
    part = part + i
    sum = sum + part

print(sum)
    