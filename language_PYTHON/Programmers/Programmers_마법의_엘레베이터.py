
def solution(storey):
    answer = 0

    storey = list(str(storey))
    flag = 0

    for index in range(len(storey) -1, -1, -1):
        val = int(storey[index])

        if flag == 1:
            val = val + 1 

        if 5 < val <= 9:
            answer = answer + 10 - val
            flag = 1 

        if val == 5:
            if index == 0:
                answer = answer + 5
            else:
                next_val = int(storey[index - 1])

                if next_val >= 5:
                    answer = answer + 10 - val
                    flag = 1
                else:
                    answer = answer + val
                    flag = 0
        
        if 1 <= val < 5:
            answer = answer + val
            flag = 0

    if int(storey[0]) > 5 or (flag and int(storey[0]) == 5):
        answer = answer + 1

    return answer

solution(555)

