import sys

def solution(queue1, queue2):
    
    n = len(queue1)
    a = queue1 + queue2

    target = sum(a)

    if target % 2 != 0:
        return -1
    
    target = target // 2

    answer = sys.maxsize
    en = 0
    tot = a[0]

    for st in range(2*n): # for 문
        while tot < target: # while 문 최대 n // 2 번 연산 가능하지 않은가? -
            en = (en + 1) % (2*n)

            tot += a[en]


        if tot == target:
            moves = 0
            if en < n - 1:
                moves = 3 * n + 1 + st + en
            else:
                moves = st + (en - n + 1)
            
            answer = min(answer, moves)
        
        tot = tot -a[st]


    if answer == sys.maxsize:
        answer = -1

    return answer

print(solution([1,2,4,2,4,2,4,5,5,5,6,5,4,4,2,6], [6,6,1,2,4,5, 2, 4, 5, 6, 12, 1, 3, 2, 4, 4]))
