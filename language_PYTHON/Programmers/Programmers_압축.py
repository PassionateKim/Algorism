def solution(msg):

    count = 27
    LZW_dict  = dict()
    for i in range(26):
        LZW_dict[chr(65 + i)] = (i + 1)

    answer = []
    input = []

    N = len(msg)

    for i in range(N):
        new = msg[i]
        input.append(new)
        next_value = "".join(input)

        if next_value not in LZW_dict:

            key = "".join(input) 
            LZW_dict[key] = count
            count = count + 1

            input.pop()

            write = LZW_dict["".join(input)]
            answer.append(write)

            # input 초기화
            input = []
            input.append(new)
    
    # 마지막 
    write = LZW_dict["".join(input)]
    
    answer.append(write)

    return answer


solution("TOBEORNOTTOBEORTOBEORNOT")
