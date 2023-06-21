# 트리순회
# 복습 횟수:0, 01:00:00, 복습필요O
import sys
si = sys.stdin.readline
tree = dict()

N = int(si())

for i in range(N):
    root, left, right = si().split()
    tree[root] = [left, right]

def preOrder(root):
    print(root, end='')

    left_child = tree[root][0]
    if(left_child != '.'):
        preOrder(left_child)

    right_child = tree[root][1]
    if(right_child != '.'):
        preOrder(right_child)
    
    return

def inOrder(root):
    left_child = tree[root][0]
    if(left_child != '.'):
        inOrder(left_child)

    print(root, end='')
    
    right_child = tree[root][1]
    if(right_child != '.'):
        inOrder(right_child)

    return

def postOrder(root):
    left_child = tree[root][0]
    if(left_child != '.'):
        postOrder(left_child)
    
    right_child = tree[root][1]
    if(right_child != '.'):
        postOrder(right_child)

    print(root, end='')

    return


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')