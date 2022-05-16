# 골드바흐의 추측
import sys

# Prime_list 만들기 0.40 초
a = [False,False] + [True] * (int(1e6)-1)
prime_list = []

for i in range(2, int(1e6)+1):
    if a[i]:
        prime_list.append(i)
        for j in range(i*i, int(1e6)+1, i):
            a[j] = False

while True:
    flag = 0
    val = int(sys.stdin.readline().rstrip())

    if val == 0:
        break
       # 둘 다 소수인 경우 체크
    for prime_num in prime_list:
        if prime_num and val - prime_num:
            print(str(val) + " = " + str(prime_num) + " + " + str(val - prime_num))
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")

     # 둘 다 소수인 경우 체크
    for idx in range(2, len(a)):
        if a[idx] and a[val - idx]:
            print(str(val) + " = " + str(idx) + " + " + str(val - idx))
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")

    # # 둘 다 소수인 경우 체크
    # for prime_num in prime_list:
    #     if val - prime_num in prime_list:
    #         print(str(val) + " = " + str(prime_num) + " + " + str(val - prime_num))
    #         flag = 1
    #         break
    # if flag == 0:
    #     print("Goldbach's conjecture is wrong.")