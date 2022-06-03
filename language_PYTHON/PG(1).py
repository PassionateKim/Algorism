N = int(input())

def solution(n):
    # 자리수 구하기
    cnt = 1
    a = pow(3, cnt)
    while True:
        if a >= n:
            break

        cnt += 1
        a += pow(3, cnt)
    
    differ = a - n 
    
    answer = ''
    tmp_change = ''

    # 각 자리수 정하기
    # 바뀔 수 있는 최대 자리수 pow(3, cnt-1)
    while True:
        if cnt == 0:
            break
        
        if differ >= pow(3, cnt-1): # 25 >= 9
            change_degree = differ // pow(3, cnt-1) # 2
            differ -= pow(3, cnt-1) * change_degree
            tmp_change += str(change_degree)
            cnt -= 1
        else:
            cnt -= 1
            tmp_change += str(0)

    for i in tmp_change:
        if i == '0':
            answer += '4'
        elif i == '1':
            answer += '2'
        else:
            answer += '1'
    print(answer)
    return answer

solution(N)