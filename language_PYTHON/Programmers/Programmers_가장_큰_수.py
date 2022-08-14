# 2022-08-13
# 2022-08-14
# 가장 큰 수
def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3 , reverse = True)
    
    answer = "".join(numbers)

    return answer

print(solution([0, 0]))