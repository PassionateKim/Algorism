from collections import deque

def solution(prices):
    answer = []

    count = len(prices) - 1
    q = deque()
    while count >= 0:
        if len(q) == 0:
            q.append([prices[count], count])
            answer.append(len(prices) - 1 - count)
            count -= 1
        else:
            while q and count >= 0:
                before_val, before_index = q[-1][0], q[-1][1]
                if before_val >= prices[count]:
                    q.pop()
                else:
                    answer.append(before_index - count)
                    q.append([prices[count], count])
                    count -= 1

    
    answer.reverse()
    
    print(answer)

    return answer

# solution([5, 4, 3, 2, 1])
solution([1, 2, 3, 2, 3])
# solution([1, 1, 1, 1, 1])