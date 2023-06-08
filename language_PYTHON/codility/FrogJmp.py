# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math
def solution(X, Y, D):
    # Implement your solution here
    diff = Y - X
    print(math.ceil(diff/D))

