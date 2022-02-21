#분해합
N = int(input())

result = 0
for i in range(1,N+1):
    A = list(map(int,str(i)))
    result = i + sum(A)
    if(result == N):
        print(i)
        break
    #체크했는데 값이 없는 경우
    elif i == N:
        print(0)