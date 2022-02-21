#분해합
N = int(input())
result = 0
for i in range(1,N+1):
    A = list(map(int,str(i)))
    result = i + sum(A)
    if(result == N):
        print(i)
        break
    elif i == N:
        print(0)