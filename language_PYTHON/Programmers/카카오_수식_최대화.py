# 2022-08-03
# 카카오 수식 최대화
from itertools import permutations


def solution(expression):
    p = permutations(["-","*","+"], 3)
    result = 0 
    for pattern in p:
        new = []
        first = expression.split(pattern[0])
        for section in first:
            second = section.split(pattern[1])
            second = [str(eval(x)) for x in second]
            new.append(pattern[1].join(second))
        print(new)
        new = [str(eval(x)) for x in new]
        print(new)
        exit()
        answer = abs(eval(pattern[0].join(new)))
        result = max(result, answer)

    return result

solution("100-200*300-500+20")