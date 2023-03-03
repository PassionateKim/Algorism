# 복습 횟수:0, 00:30:00, 복습필요X
def solution(book_time: list):
    answer = [0]
    
    book_time.sort(key=lambda x: (x[0]))
    
    for time in book_time:
        start_time, end_time = time

        s_h, s_m = start_time.split(":") 
        e_h, e_m = end_time.split(":")

        start_time = int(s_h) * 60 + int(s_m)
        end_time = int(e_h) * 60 + int(e_m)
        
        for i in range(len(answer)):
            if start_time >= answer[i] + 10: # 들어갈 수 있는 것이므로 초기화
                answer[i] = end_time
                break
            else:
                answer.append(end_time)
                break
        
        answer.sort()

    return len(answer)

solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])