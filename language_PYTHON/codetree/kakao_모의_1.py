import sys
si = sys.stdin.readline 
N = int(si())

answer = 0

while True:
    if answer > 10000:
        print(-1)
        break
    
    if N == 1:
        print(answer)
        break

    if (N % 2 == 0):
        N = N // 2
    else:
        N = N * 3 - 1
    
    answer += 1