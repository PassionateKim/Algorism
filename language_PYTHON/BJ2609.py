# 최대 공약수와 최소 공배수

N, M = map(int, input().split())
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def LCM(x, y):
    return (x * y) // GCD(x, y)

print(GCD(N,M))    
print(LCM(N,M))
