# 2022-06-xx
# 2022-07-31
# 2022-08-02
def solution(n):
    answer = ""
    a_list = ['4','1','2']
    while n > 0:

        idx = n % 3
        answer = a_list[idx] + answer
        # if n % 3 == 0:
        #     n = n - 1
        
        n = n//3

    return answer

print(solution(6))