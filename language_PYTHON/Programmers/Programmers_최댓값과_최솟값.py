# 복습 횟수:0, 00:15:00, 복습필요X 
def solution(s):
    answer = ''
    candidate = s.split()
    zzz = []
    for c in candidate:
        zzz.append(int(c))
    zzz.sort()

    answer += str(zzz[0]) + " "
    answer += str(zzz[-1])
    return answer
solution("-1 -2 -3 -4")