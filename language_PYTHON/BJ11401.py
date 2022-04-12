
n, k = map(int,input().split())
P = 1000000007

#나머지의 분배법칙을 활용해 -> 분할 정복으로 문제를 해결합니다.
#페르마의 소 정리를 활용해 -> 분모에 있는 (N-K)!(K!)-1 를 (N-K)!(K!)^p-2로 바꿔서 문제를 풉니다.

def factorial(num):
    result = 1
    for i in range(2,num+1):
        result = result * i % P
    return result

def power(num,p,mod):
    if p == 1:
        return num % mod
    
    if p % 2:
        return ((power(num,p//2,mod) ** 2) * num) % mod
    else:
        return (power(num,p//2,mod) ** 2) % mod

print(factorial(n)*power((factorial(n-k) * factorial(k)),P-2,P) % P)
