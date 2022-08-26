# 2022-08-26
# 영어 끝말잇기
def solution(n, words):
    answer = []
    word_set = set()
    # 0으로 초기화
    who = 0
    turn = 0
    idx1 = len(words)
    # 1. 같은 것을 말하는 경우
    for i in range(len(words)):
        if words[i] not in word_set:
            word_set.add(words[i])
        else:
            idx1 = i # 인덱스 저장
            break
            
    # 2. 끝말로 말하지 않는 경우
    end = words[0][-1]
    idx2 = len(words)
    for i in range(1, len(words)):
        
        start = words[i][0]
        if start != end:
            idx2 = i # 인덱스 저장
            break
        else:
            end = words[i][-1]

    # 더 앞의 것으로 계산
    i = min(idx1, idx2)
    x = i + 1 
    who = x % n
    if who == 0:
        who = n

    if x % n == 0:
        turn = x // n
    else:
        turn = (x // n) + 1  
    
    return answer

solution(2, ["hello", "one", "even", "neven", "neven", "world", "draw"])