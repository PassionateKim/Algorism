# 행렬 테두리 회전하기
def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for i in range(columns+1)] for j in range(rows+1)]
    num = 1
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            matrix[row][column] = num
            num += 1
    
    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1][y1]
        mini = tmp

        for k in range(x1, x2):
            test = matrix[k+1][y1]
            matrix[k][y1] = test
            mini = min(mini, test)

        for k in range(y1, y2):
            test = matrix[x2][k+1]
            matrix[x2][k] = test
            mini = min(mini, test)
        
        for k in range(x2,x1,-1):
            test = matrix[k-1][y2]
            matrix[k][y2] = test
            mini = min(mini, test)
        
        for k in range(y2,y1,-1):
            test = matrix[x1][k-1]
            matrix[x1][k] = test
            mini = min(mini, test)

        matrix[x1][y1+1] = tmp

    # graph = [list(i * columns + j for j in range(1, columns+1)) for i in range(rows)]
    # for i in range(len(queries)):
    #     tmp_list = []
    #     x1, y1, x2, y2 = queries[i][0]-1, queries[i][1]-1, queries[i][2]-1, queries[i][3]-1
       
       
    #     # 직사각형 위 가로 
    #     for i in range(y1, y2+1):
    #         tmp_list.append(graph[x1][i])
    #     # 직사각형 오른쪽 세로
    #     for i in range(x1+1, x2):
    #         tmp_list.append(graph[i][y2])
    #     # 직사각형 아래 가로 
    #     for i in range(y2, y1-1, -1):
    #         tmp_list.append(graph[x2][i])
    #     # 직사각형 왼쪽 세로
    #     for i in range(x2-1, x1, -1):
    #         tmp_list.append(graph[i][y1])
    #     print(tmp_list)    
    #     answer.append(min(tmp_list))


               
        

    return answer

solution(6,6,[[2,2,5,4]])