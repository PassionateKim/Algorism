def solution(elements):
    answer = set()

    N = len(elements)
    suyeol = elements + elements
    # 첫번째
    for value in elements:
        answer.add(value)

    for size in range(1, N):
        for j in range(N):
            sumi = sum(suyeol[j:j+size])
            answer.add(sumi)

    # 마지막
    answer.add(sum(elements))
    
    return len(answer)


print(solution([7, 9, 1, 1, 4]))