from collections import Counter

def solution(weight_list: list):
    answer = 0

    # 1:1, 2:3, 2:4, 3:4
    
    counter = Counter(weight_list)

    # 1.1 
    for key, value in counter.items():
        if value >= 2:
            answer = answer + (value * (value - 1)) // 2
    
    # 2:3, 2:4, 3:4
    weight_set = set(weight_list)

    new_weight_set3 = set()
    new_weight_set4 = set()
    new_weight_set5 = set()

    for weight in weight_list:
        new_weight_set3.add(weight * 3 / 2)

    for weight in weight_list:
        new_weight_set4.add(weight * 4 / 2)

    for weight in weight_list:
        new_weight_set5.add(weight * 4 / 3)


    for weight in weight_set:
        if weight in new_weight_set3:
            answer = answer + counter[weight * 2 / 3] * counter[weight] 

        if weight in new_weight_set4:
            answer = answer + counter[weight * 2 / 4] * counter[weight] 
        
        if weight in new_weight_set5:
            answer = answer + counter[weight * 3 / 4] * counter[weight] 
    
    return answer


solution([100, 180, 100, 360, 100, 270])
