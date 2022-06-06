def solution(n):
    answer = ''
    a_list = ["1","2","4"]
    
    while n > 0:
        n = n-1
        answer = a_list[n % 3] + answer
        n //= 3

    return answer
solution(10)