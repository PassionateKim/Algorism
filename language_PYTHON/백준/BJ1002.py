#터렛
import sys
si = sys.stdin.readline

for i in range(int(si())):
    x1, y1, r1, x2, y2, r2 = map(int, si().split())
    d = (abs(x1-x2)**2 + abs(y1-y2)**2)**(1/2)
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    
    
    if d > r1 + r2: # 접하지 않는 경우
        print(0)
    elif d == (r1 + r2) or d == (abs(r1 - r2)): # 접하는 경우
        print(1)
    elif abs(r1 - r2) < d < abs(r1 + r2):
        print(2) 
    