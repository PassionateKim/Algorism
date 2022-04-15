#피보나치 수 6
import sys
n = int(input())
p = 1000000007

def multi(m1,m2):
    result = [[0 for _ in range(2)] for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += m1[i][k] * m2[k][j]
                result[i][j] = result[i][j] % p
    return result

def recursive(matrix,n):
    if n == 1:
        return matrix
    elif n % 2 == 0:
        matrix = recursive(matrix, n//2)
        return multi(matrix, matrix)
    else:
        matrix = recursive(matrix, n-1)
        return multi(matrix, initial_matrix)

initial_matrix = [[1,1],[1,0]]
result_matrix = recursive(initial_matrix,n)

print(result_matrix[0][1] % p)
