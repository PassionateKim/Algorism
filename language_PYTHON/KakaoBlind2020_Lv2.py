#문자열 압축
def solution(s):
    answer = 1000
    aliquot_list = []
    answer_list = [] 
    for i in range(1,len(s)//2 + 1):
            aliquot_list.append(i)
    
    #문자열이 1개일 때 예외처리
    if(len(aliquot_list) == 0):
        aliquot_list.append(1)
    
    print("list:",aliquot_list)

    for i in aliquot_list:
        
        j = 0
        cnt = 0
        answerchar = ""
        check_char = s[:i]
        # print("시작:",check_char)
        while j+i <= len(s):
            #out of index 를 조심하기 위해 범위 설정에 신경을 씀
            if(check_char == s[j+i:j+i+i]):
                cnt += 1
            else:
                if(cnt == 0):
                    answerchar += check_char
                else:
                    answerchar += str(cnt+1)
                    answerchar += check_char
                #cnt 초기화 및 check하는 부분 변경           
                check_char = s[j+i:j+i+i]
                cnt = 0
            #기차꼬리물듯이 체크
            j += i
        #약수가 아닌 경우에 꼬리 추가
        if(len(s) % i != 0):
            answerchar = answerchar + s[len(s)-len(s)%i:]
            
            
        print(answerchar)
        answer_list.append(answerchar)

    #최소값 넣기
    for i in range(len(answer_list)):
        print(answer_list[i],"길이",len(answer_list[i]))
        if(len(answer_list[i]) < answer):
            answer = len(answer_list[i])
    

    print(answer)
    return answer

solution("a")