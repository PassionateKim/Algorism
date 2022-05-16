# 숫자 문자열과영단어
def solution(s):
    answer = s
    if answer.isdigit():
        pass
    else: # all 숫자가 아닌 경우
        if "zero" in answer:
            answer = answer.replace("zero", "0")
        if "one" in answer:
            answer = answer.replace("one", "1")
        if "two" in answer:
            answer = answer.replace("two", "2")
        if "three" in answer:
            answer = answer.replace("three", "3")
        if "four" in answer:
            answer = answer.replace("four", "4")
        if "five" in answer:
            answer = answer.replace("five", "5")
        if "six" in answer:
            answer = answer.replace("six", "6")
        if "seven" in answer:
            answer = answer.replace("seven", "7")
        if "eight" in answer:
            answer = answer.replace("eight", "8")
        if "nine" in answer:
            answer = answer.replace("nine", "9")
        
        


        

    return int(answer)

print(solution("one4seveneight"))