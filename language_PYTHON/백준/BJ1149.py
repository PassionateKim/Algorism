# RGB 거리
import sys
si = sys.stdin.readline

N = int(si())
RED = []
GREEN = []
BLUE = []

for i in range(N):
    r, g, b = map(int, si().split())
    RED.append(r)
    GREEN.append(g)
    BLUE.append(b)

# DP로 계산하기
for i in range(1, N):
    RED[i] = min(GREEN[i-1] + RED[i], BLUE[i-1] + RED[i]) 
    GREEN[i] = min(RED[i-1] + GREEN[i], BLUE[i-1] + GREEN[i]) 
    BLUE[i] = min(RED[i-1] + BLUE[i], GREEN[i-1] + BLUE[i]) 
print(min(RED[N-1],GREEN[N-1], BLUE[N-1]))