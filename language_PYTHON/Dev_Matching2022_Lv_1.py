
def solution(lottos, win_nums):
    #값 초기화
    lottos = lottos
    win_nums = win_nums
    correct_list = []

    zero_num = 0
    correct = 0
    
    #0은 당첨숫자가 절대 아니므로
    for i in lottos:
        if(i == 0):
            zero_num += 1
        else:
            if(i in win_nums):
                correct += 1
                correct_list.append(i)
    #최저 순위 번호 rank
    worst_rank = 0
    if(2 <=correct<= 6):
        worst_rank = 7 - correct
    else:
        worst_rank = 6 
    
    #최고순위번호
    best_rank = 0
    #예외처리
    if(worst_rank == 6 and correct == 0):
        best_rank = worst_rank - zero_num 
    else:
        best_rank = worst_rank - zero_num
    
    answer = [best_rank,worst_rank]
    print(answer)
    return answer

solution([1,2,3,4,5,6],[7,8,9,10,11,12])