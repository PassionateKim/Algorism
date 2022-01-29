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

all_list = list(range(2,246912))
prime_list = []

for i in all_list:
    if isPrime(i):
        prime_list.append(i)


while True:
    M = int(input())
    if(M == 0):
        break
    N = 0       
    for i in prime_list:
        if M < i <= M*2:
            N += 1
    print(N)
