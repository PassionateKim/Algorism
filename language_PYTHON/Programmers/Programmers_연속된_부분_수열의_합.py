# 2023-07-01
# 2023-07-12
# 복습 횟수:1, 00:30:00, 복습필요:* (3번째에 맞으면 끝)
def solution(sequence, k):
    candidate = []

    def slidingWindow(candidate: list, sequence, k):
        start = 0
        end = 0
        sumi = sequence[0]
        while (start <= end and start != len(sequence) and end != len(sequence)):
            if sumi >= k:
                if sumi == k:
                    candidate.append([start, end])
                
                sumi = sumi - sequence[start]
                start += 1
            else: # sumi < k:
                end += 1
                if end != len(sequence):
                    sumi = sumi + sequence[end]

        return
    
    slidingWindow(candidate, sequence, k)
    candidate.sort(key=lambda x: [x[1] - x[0], x[0]])
    return candidate[0]

solution([1, 1, 1,2, 3, 4, 5], 5)