# 2022-08-26
# 2022-08-27
# 영어 끝말잇기
def solution(n, words):
    answer = []
    candidate_list = list()
    candidate_list.append(words[0])
    check = len(words)+1
    for i in range(1, len(words)):
        # 탈출조건
        if candidate_list[-1][-1] != words[i][0]:
            check = i
            break
        if words[i] in candidate_list:
            check = i
            break
        
        candidate_list.append(words[i])

    # 조건이 없는 경우
    if check == len(words)+1:
        answer.append(0)
        answer.append(0)
        return answer
    else: #조건이 있는 경우
        x = check + 1 
        who = x % n
        
        if who == 0:
            who = n

        
        turn = x // n
        if (x%n) != 0:
            turn += 1

    answer.append(who)
    answer.append(turn)
    print(answer)

    return answer

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "tank", "tank"])