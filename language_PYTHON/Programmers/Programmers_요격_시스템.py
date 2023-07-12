# 2023-06-30
# 2023-07-12
# 복습 횟수:1, 00:30:00, 복습필요:*(세 달 뒤 쯤 복습하면 될듯 - 그때도 맞으면 끝)
def solution(targets: list):
    answer = 0
    targets.sort(key=lambda x: x[1])
    end = 0

    for target in targets:
        if target[0] >= end:
            answer += 1
            end = target[1]


    return answer

solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])
