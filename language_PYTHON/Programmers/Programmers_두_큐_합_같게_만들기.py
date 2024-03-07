from collections import deque

def solution(queue1, queue2):
    answer = 0

    
    # 합이 홀수라면 어차피 안되므로 
    if(sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)


    count = 0 
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)

    n = len(queue1)
    while count <= n * 4:

        if q1_sum == q2_sum:
            return answer
        
        if q1_sum > q2_sum:
            val = queue1.popleft()
            queue2.append(val)

            q1_sum -= val
            q2_sum += val

        else:
            val = queue2.popleft()
            queue1.append(val)

            q1_sum += val
            q2_sum -= val

        count += 1
        answer += 1

    return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1] ))
