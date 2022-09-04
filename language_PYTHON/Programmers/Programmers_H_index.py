# 2022-09-04
# 2022-09-05
# H-Index
def isHindex(h, array):
    cnt = 0
    for i in range(len(array)):
        if array[i] >= h:
            # h이상인 논문의 개수
            cnt = len(array) - i
            break
    # h번 이상 인용된 논문이 h편 이상인지 체크
    if cnt >= h:
        return True

    return False

def solution(citations):
    answer = 0
    citations.sort()
    start, end = 0, len(citations)

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(len(citations)):
            if citations[i] >= mid:
                # h 이상인 논문의 개수
                cnt = len(citations) - i
                break
        if cnt >= mid:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer

print(solution([1, 1, 1, 1, 1]))