# 2023-06-20
# 복습 횟수:1, 01:00:00, 복습필요O
import sys
si = sys.stdin.readline

def toPostOrder(preOrder: list, inOrder: list):
    if(len(preOrder) == 0):
        return
    
    if (len(preOrder) == 1):
        print(preOrder[0], end=' ')
        return
    # 길이에 따른 분기가 필요함
    root = preOrder[0]
    
    index = inOrder.index(root)
    
    left_preOrder = preOrder[1:1+index]
    left_inOrder = inOrder[:index]
    toPostOrder(left_preOrder, left_inOrder)

    right_preOrder = preOrder[1+index:]
    right_inOrder = inOrder[index+1:]
    toPostOrder(right_preOrder, right_inOrder)

    print(preOrder[0], end=' ')    

    return

T = int(si())
for i in range(T):
    N = int(si())
    
    for j in range(2):
        if (j == 0):
            preOrder = list(map(int, si().split()))
        else:
            inOrder = list(map(int, si().split()))
    
    toPostOrder(preOrder, inOrder)
    print()