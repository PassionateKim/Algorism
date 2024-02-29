def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0: # 짝수인 경우
            answer.append(number + 1)
        else: # 홀수인 경우
            number_bin = bin(number)[2:]
            if number_bin[0] == '1':
                number_bin = '0' + number_bin
            
    
            last_zero_index = 0
            for i in range(len(number_bin)):
                if number_bin[i] == '0':
                    last_zero_index = i
            
            number_bin = list(number_bin)
            number_bin[last_zero_index] = '1'
            number_bin[last_zero_index + 1] = '0'

            number_bin = "".join(number_bin)

            answer.append(int(number_bin, 2))

    return answer

solution([2, 7])