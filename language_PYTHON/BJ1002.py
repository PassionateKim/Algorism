# #터렛
# import math
# T = int(input())

# for i in range(T):
#     x1, y1, r1, x2, y2, r2 = map(int,input().split())
#     distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
#     if(distance == 0 and r1 == r2):
#         print(-1)
#     elif(distance>(r1+r2) or distance<abs(r1-r2)):
#         print(0)
#     elif(distance==(r1+r2) or distance==abs((r1-r2))):
#         print(1)
#     elif(distance<(r1+r2) or distance>abs(r1-r2)):
#         print(2)    

 
    
#터렛

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    if(x1==x2 and y1==y2 and r1 == r2):
        print(-1)
    elif(((x1-x2)**2+(y1-y2)**2)>(r1+r2)**2): 
        print(0)
    elif(((x1-x2)**2+(y1-y2)**2)==(r1+r2)**2):
        print(1)
    elif(((x1-x2)**2+(y1-y2)**2)<(r1+r2)**2):
        print(2)
    elif(((x1-x2)**2+(y1-y2)**2)<(r1-r2)**2):
        print(0)    
    
    elif(((x1-x2)**2+(y1-y2)**2)==(r1-r2)**2):
        print(1)