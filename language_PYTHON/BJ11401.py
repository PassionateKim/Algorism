def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % 122
    return n
def factorial2(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) 
    return n % 122


print(factorial(11))
print(factorial2(11))