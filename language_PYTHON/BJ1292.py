#쉽게 푸는 문제

sum = 0
value_list = []

A,B = map(int,input().split())

#기준값

na = 1
nb = 1
#A 위치 특정하기
while True:
    a = (na*(na+1)//2)

    if(a < A):
        na += 1
    else:
        # print("기준값: "+ str(na)+" 위치 차이: "+ str(A-a))   
        break

#B 위치 특정하기
while True:
    b = (nb*(nb+1)//2)

    if(b < B):
        nb += 1
    else:
        # print("기준값: "+ str(nb)+" 기준으로부터의 위치: "+ str((B-b)))
        break

#sum_B
sum_of_sequence_B = (nb)*(nb+1)*(2*nb+1)//6
sum_B =  sum_of_sequence_B - abs(B-b)*nb
# print(sum_B)

#sum_A
sum_of_sequence_A = (na)*(na+1)*(2*na+1)//6
sum_A =  sum_of_sequence_A - abs(A-a)*na - na
# print(sum_A)

answer = sum_B - sum_A
print(answer)