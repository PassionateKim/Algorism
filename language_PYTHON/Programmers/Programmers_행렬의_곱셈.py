def solution(arr1, arr2):
    answer = []
    
    N = len(arr1)
    M = len(arr1[0])
    K = len(arr2[0])

    for n in range(N):
        tmp = []
        for k in range(K):
            sumi = 0
            for m in range(M):
                sumi = sumi + (arr1[n][m] * arr2[m][k])
            tmp.append(sumi)
        answer.append(tmp)

    return answer

solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])