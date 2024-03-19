from collections import Counter
def solution(weight_list: list):
    answer = 0

    counter = Counter(weight_list)
    
    for key, value in counter.items():
        if value >= 2:
            answer = answer + value * (value - 1) // 2

    weight_set = set(weight_list)

    for weight in weight_set:
        if (weight * 2) / 3 in weight_set:
            answer += counter[weight * 2 / 3] * counter[weight]

        if (weight * 2) / 4 in weight_set:
            answer += counter[weight * 2 / 4] * counter[weight]
        
        if (weight * 3) / 4 in weight_set:
            answer += counter[weight * 3 / 4] * counter[weight]

    return answer


solution([100,180,360,100,270])