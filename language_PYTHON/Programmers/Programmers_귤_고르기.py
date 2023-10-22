from collections import defaultdict

def solution(k, tangerine):
    answer = 0

    check_number = defaultdict(int)

    for t in tangerine:
        check_number[t] += 1


    check_number = sorted(check_number.items(), key = lambda x: x[1], reverse= True)    
    cursor = 0
    while k > 0:
        k = k - check_number[cursor][1]
        answer += 1
        cursor += 1
    
    return answer