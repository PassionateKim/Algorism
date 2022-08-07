# 2022-06-xx
# 2022-07-31
# 2022-08-02
# 2022-08-07

# 4,5,6 나라의 숫자
def solution(n):
    answer = ""
    num = ["6", "4", "5"]
    
    while n >= 1:
        # 예외조건
        answer = num[n%3] + answer
        
        # if n % 3 == 0:
        #     n = n - 1
        
        n = n // 3

    return answer

print(solution(9))