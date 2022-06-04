n = 9 
n //= 3
print(n)

# def solution(n):
#     answer = ''
#     a_list = ["1","2","4"]
    
#     while n > 0:
#         n = n-1
#         answer = a_list[n % 3] + answer
#         n //= 3

#     return answer
# solution(10)


# n = n // 3 으로 하면 효율성 TC 틀리는데
# n //= 3 은 효율성 TC 틀리지 않음...?? 
# 이유가 무엇인지 
