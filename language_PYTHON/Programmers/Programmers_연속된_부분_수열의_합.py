# 복습 횟수:0, 01:00:00, 복습필요O
# 2023-07-01

def slidingWinodw(sequence, answer: list, k):
    left, right= 0, 0
    sumi = sequence[0] # 초기값
    
    while (left != len(sequence) and right != len(sequence)):
        
        if(sumi <= k):
            if(sumi == k):
                answer.append([left, right])

            right += 1
            if(right == len(sequence)): return
            sumi += sequence[right]

        else:
            sumi -= sequence[left]
            left += 1
    
    return

def solution(sequence, k):
    answer = []
    slidingWinodw(sequence, answer, k)

    answer.sort(key= lambda x: [abs(x[1] - x[0]), x[0]])

    return answer[0]

solution([1, 1, 1, 2, 3, 4, 5], 5)
