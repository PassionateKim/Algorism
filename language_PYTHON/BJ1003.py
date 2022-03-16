#피보나치 수열 DP
import time

def fibo(x):
    if x == 1 or x == 2:
        return 1

    return fibo(x-1) + fibo(x-2)

print("재귀함수 활용")
for num in range(5,40,10):
    start = time.time()
    res = fibo(num)
    print(res,"->런닝타임",round(time.time()-start,2),'초')
print("------------------")

print("top-down DP 활용")
d = [0] * 50
def fibo2(x):
    if x == 1 or x == 2:
        return 1
    # if d[x] != 0:
    #     return d[x]
    d[x] = fibo2(x-1) + fibo2(x-2)
    return d[x]

for num in range(5, 40, 10):
    start = time.time()
    res = fibo2(num)
    print(res, '-> 러닝타임:', round(time.time() - start, 2), '초')
print("------------------")

print("bottom-up DP 활용")
for num in range(5,40,10):
    d = [0]*100
    d[0] = 1
    d[1] = 1
    start = time.time()
    for i in range(2,num):
        d[i] = d[i-1]+d[i-2]
    print(d[num-1],num,"->런닝타임",round(time.time()-start,2),'초')
print("------------------")

