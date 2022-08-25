# 2022-08-25
# 카펫
def solution(brown, yellow):
    # [가로, 세로]
    answer = []
    # x>=3 y>=3 x>=y
    candidate_list = list() 
    # 1. 후보군 넣기
    y = 3
    x = brown//2 + 2 - y
    
    while x >= y:
        candidate_list.append([x, y])
        x -= 1
        y += 1

    while candidate_list:
        x, y = candidate_list.pop()
        if (x-2) * (y-2) == yellow:
            answer.append(x)
            answer.append(y)
            break
    print(answer)
    return answer

solution(24, 24)