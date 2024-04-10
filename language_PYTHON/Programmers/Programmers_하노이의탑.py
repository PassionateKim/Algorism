answer = []

def hanoi(n, start, end, mid):
    
    if n == 1:
        answer.append([start, end])    
        return
    
    hanoi(n-1, start, mid, end)
    hanoi(1, start, end, mid)
    hanoi(n-1, mid, end, start)

def solution(n):

    hanoi(n, 1, 3, 2)
    return answer


solution(2)