def solution(n):
    answer = 0

    window = [i for i in range(1, n+1)]
    
    sumi = 0
    left = 0
    right = 0

    while left <= right:
        
        if sumi >= n:
            if sumi == n:
                answer = answer + 1
            
            sumi = sumi - window[left]
            left = left + 1 
            
        else: # sumi < n
            if right == n:
                break

            sumi = sumi + window[right]
            right = right + 1

    return answer


print(solution(15))