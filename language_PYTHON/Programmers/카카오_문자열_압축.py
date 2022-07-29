# 2022-06-06
# 2022-07-29
# 문자열 압축

def solution(s):
    answer = 1000
    
    # 체크할 길이
    if len(s) == 1:
        return len(s)

    for i in range(1, len(s)//2 + 1):
        i = 2
        tmp = s[0:i]
        cnt = 1
        tmp_str = ""
        for j in range(i, len(s)+1, i):
            check = s[j:j+i]
            # 같으면
            if tmp == check:
                cnt += 1
                
            else: # 다르면
                # 하나일 때는 포함하지 않는다.
                if cnt != 1:
                    tmp_str += (str(cnt) + tmp)
                elif cnt == 1:
                    tmp_str += tmp    
                # tmp를 바꿔준다.
                tmp = check
                cnt = 1 # 초기화
            
        # 마무리
        check = s[j:]
        # 꼬리 체크
        # 개수가 다른 경우     
        if len(check) != i: 
                tmp_str += check
        # 개수가 같은 경우 어떤 경우든 나머지를 넣어야하므로
        else:
            if cnt != 1:
                    tmp_str += (str(cnt) + tmp)
            else:
                tmp_str += tmp
        
        answer = min(answer, len(tmp_str))    
    
    # /체크 
    return answer

solution("abcabcabcabcdededededede")
# solution("aabbaccc")