#베르트랑 공준 


def isPrime(n):
    if(n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
             return False
        return True



while True:
    M = int(input())
    if(M == 0):
        break
    N = 0       
    for i in range(M+1,2*M+1):
        if(isPrime(i)):
            N = N+1
    print(N)
