# 복습 횟수:0, 01:00:00, 복습필요O
import sys
si = sys.stdin.readline

def toPostorder(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end = ' ')
        return
    
    root_idx = inorder.index(preorder[0])
    left_inorder = inorder[0:root_idx]
    left_preorder = preorder[1: 1+len(left_inorder)]
    toPostorder(left_preorder, left_inorder)

    right_inorder = inorder[root_idx+1:]
    right_preorder = preorder[1 + len(left_preorder):]
    toPostorder(right_preorder, right_inorder)

    print(preorder[0], end=' ')




T = int(si())
for i in range(T):
    N = int(si())
    for i in range(2):
        if i == 0:
            preorder = list(map(int, si().split()))
        else:
            inorder = list(map(int, si().split()))

    toPostorder(preorder, inorder)
    