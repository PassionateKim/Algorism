from collections import deque
def solution(numbers):
    answer = []
    
    big_stack = deque()
    count = len(numbers) - 1
    while count >= 0:
        if len(big_stack) == 0:
            big_stack.append(numbers[count])
            answer.append(-1)
            count -= 1
            continue

        if numbers[count] > big_stack[-1]:
            big_stack.pop()
        elif numbers[count] == big_stack[-1]:
            big_stack.pop()
        else:
            answer.append(big_stack[-1])
            big_stack.append(numbers[count])
            count -= 1

    answer.reverse()
    return answer


solution([9, 1, 5, 3, 6, 2]	)