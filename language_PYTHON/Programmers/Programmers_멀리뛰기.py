
def solution(n):
    answer = 0
    # 한칸, 두칸 을 갈 수 있다.
    # 입력으로 우리는 최대 몇 개의 2가 존재할 수 있는지 알 수 있다.
    # 문제를 바꿀 수 있음 Combination으로 위치 ... ]
    if (n == 1):
        return 1
    
    if (n == 2):
        return 2
    
    max_two = n // 2
    for number_of_two in range(max_two, -1, -1):
        left = n - (number_of_two * 2) 
        total = left + number_of_two # n

        total_sum = 1
        left_sum = 1

        counter = 0
        while counter < number_of_two:
            total_sum = total_sum * (total - counter)
            left_sum = left_sum * (number_of_two - counter)

            counter = counter + 1        
        
        answer = answer + (total_sum // left_sum)
        answer = answer % 1234567

    return answer

print(solution(3))