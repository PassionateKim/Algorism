def solution(n):
    answer = []

    def hanoi(n, start, end, sub):
        if n == 1:
            answer.append([start, end])
            return
        
        hanoi(n-1, start, sub, end)
        hanoi(1, start, end, sub)
        hanoi(n-1, sub, end, start)


    hanoi(n, 1, 3, 2)
    return answer

solution(3)