# RGB 거리
import sys
si = sys.stdin.readline 
N = int(si())

dp_rgb = [[0, 0, 0] for i in range(N)]
for i in range(N):
    red, green, blue = map(int, si().split())
    
    if i == 0:
        dp_rgb[0][0] = red
        dp_rgb[0][1] = green
        dp_rgb[0][2] = blue
    else:
        dp_rgb[i][0] = min(red + dp_rgb[i-1][1], red + dp_rgb[i-1][2])
        dp_rgb[i][1] = min(green + dp_rgb[i-1][0], green + dp_rgb[i-1][2])
        dp_rgb[i][2] = min(blue + dp_rgb[i-1][0], blue + dp_rgb[i-1][1])

print(min(dp_rgb[N-1])) 