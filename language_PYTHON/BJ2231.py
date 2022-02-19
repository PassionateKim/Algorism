#분해합

flag = 0
def check_constructor(N):
    global flag
    max_digit = N
#1,000,000 백만이 최대이므로 생성자는 최대 5자리수
#중복이 가능해야 하므로 -> 배열을 활용

#생성자의 최대 자리수 구하기
    e = 1
    while max_digit >= 10:
      e += 1
      max_digit = max_digit//10
    
#자리수 e-1부터 e까지만 체크하면 됨
#ex) 108 = 99 + 9 + 9 ,  1026 = 999 + 9 + 9 + 9, ... 더해봤자 한자리 이상 넘어갈수 없기 때문

#case1 1<= N < 100

#case1)-1 홀수인 경우
#1의 자리수의 홀수는 작은 생성자가 없음
    if(N<10 and N%2 == 1):
        print(0)
        flag = 1
        return
    elif(10<=N<100 and N%2 == 1):
        for i in range(1,9+1):
            for j in range(0,9+1):
                if(11*i + 2*j == N):
                    print(10*i+j)  
                    flag = 1
                    return         
#case1)-2 짝수인 경우
# 18까지는 그냥 2로 나누면 됨    
    elif(N<=18 and N%2 == 0):
        print(N//2)
        flag = 1
        return
    elif(18<N<100 and N%2 == 0):
        for i in range(1,9+1):
            for j in range(0,9+1):
                if(11*i + 2*j == N):
                    print(10*i+j) 
                    flag = 1
                    return
                    

    

    #case2 100<= N < 1000
    #case2)-1 생성자가 2자리 수 인 경우 99 + 9 + 9 = 117이므로 최대 117의 값을 가진다.
    elif(100<=N<=117):
        for i in range(1,9+1):
            for j in range(0,9+1):
                if(11*i + 2*j == N):
                    print(10*i+j) 
                    flag = 1
                    return
    #case2)-2 생성자가 3자리 수 인 경우
    elif(118<=N<1000):
        for i in range(1,9+1):
            for j in range(0,9+1):
                for k in range(0,9+1):
                    if(101*i+11*j+2*k == N):
                        print(100*i+10*j+k)
                        flag = 1
                        return





    
        
N = int(input())

check_constructor(N)
if flag == 0:
    print(0)
# #자리수 2개
# print(N//10,N%10)
# #자리수 3개
# print(N//10//10,N//10%10, N%10)
# #자리수 4개
# print(N//10//10//10,N//10//10%10, N//10%10,N%10)
# #자리수 5개
# print(N//10//10//10//10,N//10//10//10%10, N//10//10%10,N//10%10,N%10)

