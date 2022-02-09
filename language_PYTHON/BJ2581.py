#2581소수

#소수 구하기 함수
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

#for 문을 계속 돌리면 시간초과 나므로, 미리 소수를 배열에 넣어두기
for i in all_list:
    if isPrime(i):
        prime_list.append(i)

M = int(input())
N = int(input())

#배열의 인덱스, sum을 활용하는 아이디어 
specific_prime_list = []
for i in range(M,N+1):
    if(i in prime_list):
        specific_prime_list.append(i)

if len(specific_prime_list) == 0:
    print(-1)
else:
    print(sum(specific_prime_list))
    print(specific_prime_list[0])
