def solution(n, k):
    answer = []
    
    candidate = [ i for i in range(1, n + 1) ]
    

    for i in range(n-1, 0, -1):
        # 1. divider init
        divider = 1
        for j in range(1, i + 1):
            divider = divider * j
        
        val = (k - 1) // divider
        appendable = candidate[val]
        answer.append(appendable)

        candidate.remove(appendable)
        k = k - (divider * val)

    answer.extend(candidate)
    return answer

solution(5, 41)