def solution(number, k):

    answer = []
    
    for num in number:
        while k and answer and num > answer[-1]:
            k -= 1
            answer.pop()

        answer.append(num)

    if k > 0:
        answer = answer[:len(number) - k]
    
    return "".join(answer)

# solution("21", 1) # 2
# solution("19", 1) # 9
# solution("1924", 2)
solution("13579", 3) 
solution("98765", 3) # 98 
solution("4177", 2) # 77

solution("4577252841", 4)
solution("4177252841", 4)
# 제거 했을 때 가장 큰 수가 되도록 
# 10 , 4 -> 6 반드시 6자리임 여기서 힌트를 좀 얻을 수 있을 것같긴 한데.. 
 
# 앞자리가 반드시 커야 함
# 775841 #

# 반드시 왼쪽이 기준  시점인것 중에 가장 항상 커야함

# "4577252841"	4	"775841"