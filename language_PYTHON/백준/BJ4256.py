# 2023-06-17
# 2023-06-20
# 2023-07-27
# 복습 횟수:2, 01:30:00, 복습필요O

import sys
si = sys.stdin.readline 
T = int(si())

def post_order(pre_order : list, in_order: list):
   
    if len(pre_order) == 0:
        return
   
    if len(pre_order) == 1:
        print(pre_order[0], end = " ")
        return

    root = pre_order[0]
    root_index = in_order.index(root)

    left_inorder = in_order[:root_index]
    right_inorder = in_order[root_index+1:]

    left_preorder = pre_order[1:1+len(left_inorder)]
    right_preorder = pre_order[1+len(left_inorder):]

    post_order(left_preorder, left_inorder)
    post_order(right_preorder, right_inorder)

    print(root, end = " ")
    return

for i in range(T):
    N = int(si()) # node의 개수

    pre_order = list(map(int, si().split()))
    in_order = list(map(int, si().split()))

    post_order(pre_order, in_order)
    print()