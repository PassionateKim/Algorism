# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    pass
    visited = [0 for i in range(len(A)+2)]
    visited[0] = 1
    for val in A:
        visited[val] = 1 # 방문 처리

    return visited.index(0)


solution([2, 3, 1, 5])