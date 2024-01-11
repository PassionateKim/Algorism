from collections import defaultdict

def solution(want, number, discount):
    answer = 0

    n = sum(number)

    # init_dict
    my_dict = defaultdict(int)
    for key, value in zip(want, number):
        my_dict[key] = value

    check_dict = defaultdict(int)
    for i in range(n):
        key = discount[i]
        check_dict[key] = check_dict[key] + 1
    
    
    if(my_dict == check_dict):
        answer += 1
        
    for index in range(len(discount) - n):
        
        # left subtract
        subtract_key = discount[index]
        check_dict[subtract_key] -= 1

        if(check_dict[subtract_key] == 0):
            del check_dict[subtract_key]

        # right add
        add_index = n + index
        add_key = discount[add_index]
        check_dict[add_key] += 1

        if(my_dict == check_dict):
            answer += 1
        
    return answer


solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])