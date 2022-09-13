# 2022-09-13
# n^2 배열 자르기
def solution(n, left, right):
    answer = []
    for i in range(left, right+ 1):
        q = (i+1) // n
        r = (i+1) % n
        print("i:",i,"일때:","몫:",q,"나머지:",r)

    return answer

solution(4, 7, 14)