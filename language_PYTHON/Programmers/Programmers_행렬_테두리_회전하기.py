# 행렬 테두리 회전하기
def solution(rows, columns, queries):
    result = []
    graph = [[i + j * columns for i in range(1, columns+1)] for j in range(rows)]
    for i in graph:
        print(i)
    for x1, y1, x2, y2 in queries:
        stack = []
        r1, c1, r2, c2 = x1-1, y1-1, x2-1, y2-1
        # 위 가로
        for i in range(c1, c2+1):
            if i == c1:
                stack.append(graph[r1][i])
            else:
                stack.append(graph[r1][i])
                graph[r1][i] = stack[-2]
        # 오른 세로
        for i in range(r1+1,r2+1):
            stack.append(graph[i][c2])
            graph[i][c2] = stack[-2]
        # 아래 왼쪽
        for i in range(c2-1, c1-1, -1):
            stack.append(graph[r2][i])
            graph[r2][i] = stack[-2]
        # 위로
        for i in range(r2-1, r1-1, -1):
            stack.append(graph[i][c1])
            graph[i][c1] = stack[-2]
        for i in graph:
            print(i)

        






    return result

solution(6, 6, [[2,2,5,4]])