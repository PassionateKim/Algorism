# 카펫
# 복습 횟수:1, 00:15:00, 복습필요X
def solution(brown, yellow):
    answer = []
    sero = 1
    while sero <= (yellow + 1) // 2:        
        if yellow % sero == 0: # 나눠진다면
            garo = yellow // sero

            check = (sero + garo) * 2 + 4
            if check == brown:
                answer.append([garo+2, sero+2])
                break
        else:
            pass

        sero += 1

    return answer[0]

print(solution(8, 1))