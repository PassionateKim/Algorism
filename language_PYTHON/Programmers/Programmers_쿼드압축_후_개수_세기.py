zero = 0
one = 0

def divide_conquer(arr, x, y, n):
    global zero
    global one 

    check = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != check:
                divide_conquer(arr, x, y, n // 2)
                divide_conquer(arr, x + n // 2, y, n // 2)
                divide_conquer(arr, x, y + n // 2, n // 2)
                divide_conquer(arr, x + n // 2, y + n // 2, n // 2)

                return 
            
    if check == 0:
        zero += 1
    else:
        one += 1

def solution(arr):
    answer = []

    divide_conquer(arr, 0, 0, len(arr))

    answer.append(zero)
    answer.append(one)

    return answer


solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])