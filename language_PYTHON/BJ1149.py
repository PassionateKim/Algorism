# RGB 거리
import sys
input = sys.stdin.readline
N = int(input().rstrip())
RGB = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    RGB[i][0] += min(RGB[i-1][1], RGB[i-1][2])
    RGB[i][1] += min(RGB[i-1][0], RGB[i-1][2])
    RGB[i][2] += min(RGB[i-1][0], RGB[i-1][1])
print(min(RGB[i][0],RGB[i][1],RGB[i][2]))


#3P2 * 2**(N-1) 에서 복잡도를 더 줄일 아이디어??.
# 이미 정해진 값은 for문을 쓰지 않는 방향으로 생각하기
# bottom up이 안되면 top down으로도 사고하기