#골드바흐의 추측
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

all_list = list(range(2,10000))
prime_list = []

for i in all_list:
    if isPrime(i):
        prime_list.append(i)



T = int(input())

for i in range(1,T+1):
    n = int(input())
    half = n//2
    for j in range(half,1,-1):
        if(j in prime_list) and (n-j in prime_list):
            print(j, n-j)
            break
        

    




