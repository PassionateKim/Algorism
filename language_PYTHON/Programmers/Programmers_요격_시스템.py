# 2023-06-30
# 복습 횟수:0, 01:00:00, 복습필요O

def solution(targets: list):
    answer = 0
    
    targets.sort(key = lambda x: x[1])

    s = e = 0
    for target in targets:
        if target[0] >= e:
            answer += 1
            e = target[1]
        
    return answer

solution([[1,4], [4,5], [4,8], [10,14], [11,13] ,[5, 12], [3, 7]])
