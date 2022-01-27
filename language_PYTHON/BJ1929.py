#1929번 소수 구하기  에라토스테네스의 체




M,N = input().split()


M = int(M)
N = int(N)


def isPrime(n):
    if(n == 2):
        return True
    elif (n == 1):
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
             return False
        return True


for i in range(M,N+1):
    if(isPrime(i)):
        print(i)