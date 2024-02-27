from collections import defaultdict
def solution(topping):
    answer = 0
    right_dict = defaultdict(int)
    left_dict = defaultdict(int)

    # O(N)
    for tp in topping:
        right_dict[tp] += 1
    
    
    for tp in topping:
        left_dict[tp] += 1
        right_dict[tp] -= 1

        if right_dict[tp] == 0:
            del right_dict[tp]
        
        if len(left_dict) == len(right_dict):
            answer += 1

    return answer


solution([1, 2, 1, 3, 1, 4, 1, 2])