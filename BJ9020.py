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

print(prime_list)

T = int(input())

for i in range(1,T+1):
    n = int(input())
    print("예제입력: "+str(n))
    




