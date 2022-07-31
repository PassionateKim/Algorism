# 2022-06-xx
# 2022-07-31
def solution(n):
    answer = ''
    a_list = ["4","1","2"]
    
    while n > 0:
        answer = a_list[n%3] + answer
        if(n%3 == 0):
            n = (n//3) - 1
        else:
            n = (n//3)
    
    return answer

print(solution(9))