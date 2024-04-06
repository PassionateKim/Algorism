def solution(data: list, col, row_begin, row_end):
    answer = 0
    data.sort(key= lambda x:[x[col-1], -x[0]])

    S = []

    for index, val in enumerate(data):
        tmp = 0
        
        for i in val:
            tmp = tmp + i % (index + 1)
        S.append(tmp)
    
    prefix = S[row_begin - 1]
    for i in range(row_begin, row_end):
        prefix = prefix ^ S[i]
    
    print(prefix)
        
    return answer



solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]]	, 2, 2, 3)