from collections import deque
def solution(progresses, speeds):
    progressq = deque(progresses)
    speedq = deque(speeds)
    answer = []
    time = 0
    count = 0

    while progressq:
        if progressq[0] + time * speedq[0] >= 100:
            progressq.popleft()
            speedq.popleft()
            count += 1
        else:
            if count >= 1:
                answer.append(count)
                count = 0 # 0으로 초기화
            
            time += 1
    answer.append(count)
    return answer

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])