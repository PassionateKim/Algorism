# 복습 횟수:0, 00:30:00, 복습필요X
def solution(s):
    answer = []
    cnt = 0
    zero_num = 0 
    while True:
        if s == '1':
            answer = [cnt, zero_num]
            break
        tmp = ''
        for x in s:
            if x == '1':
                tmp += '1'
            else:
                zero_num += 1
        
        check = len(tmp)
        
        new_s = ''
        while check != 0:
            new_s = str((check % 2)) + new_s
            check = check // 2
        
        s = new_s
        cnt += 1

    return answer


solution("110010101001")