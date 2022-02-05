#네 번째 점
X1, Y1 = map(int,input().split())
X2, Y2 = map(int,input().split())
X3, Y3 = map(int,input().split())


#대각선

#대각선이 x1 y1  x2 y2 쌍인 경우
if((max(abs((X1-X2)**2+(Y1-Y2)**2),abs((X1-X3)**2+(Y1-Y3)**2),abs((X2-X3)**2+(Y2-Y3)**2)))==abs((X1-X2)**2+(Y1-Y2)**2)):
   #x3,y3가 좌측 하단인 경우
    if(min(X1,X2,X3)==X3 and min(Y1,Y2,Y3)==Y3):  
        print(max(X1,X2,X3),max(Y1,Y2,Y3))
    #x3,y3이 좌측 상단인 경우
    elif(min(X1,X2,X3)==X3 and max(Y1,Y2,Y3)==Y3):  
        print(max(X1,X2,X3),min(Y1,Y2,Y3))
    #x3,y3이 우측 상단인 경우
    elif(max(X1,X2,X3)==X3 and max(Y1,Y2,Y3)==Y3):  
        print(min(X1,X2,X3),min(Y1,Y2,Y3))
    #x3,y3이 우측 하단인 경우
    else:
        print(min(X1,X2,X3),max(Y1,Y2,Y3))
    
    
#대각선이 x1 y1  x3 y3 쌍인 경우     
elif((max(abs((X1-X2)**2+(Y1-Y2)**2),abs((X1-X3)**2+(Y1-Y3)**2),abs((X2-X3)**2+(Y2-Y3)**2)))==abs((X1-X3)**2+(Y1-Y3)**2)):
    #x2,y2가 좌측 하단인 경우
    if(min(X1,X2,X3)==X2 and min(Y1,Y2,Y3)==Y2):  
        print(max(X1,X2,X3),max(Y1,Y2,Y3))
    #x2,y2이 좌측 상단인 경우
    elif(min(X1,X2,X3)==X2 and max(Y1,Y2,Y3)==Y2):  
        print(max(X1,X2,X3),min(Y1,Y2,Y3))
    #x2,y2이 우측 상단인 경우
    elif(max(X1,X2,X3)==X2 and max(Y1,Y2,Y3)==Y2):  
        print(min(X1,X2,X3),min(Y1,Y2,Y3))
    #x2,y2이 우측 하단인 경우
    else:
        print(min(X1,X2,X3),max(Y1,Y2,Y3))
    
    
#대각선이 x2 y2  x3 y3 쌍인 경우
else:
    #x1,y1가 좌측 하단인 경우
    if(min(X1,X2,X3)==X1 and min(Y1,Y2,Y3)==Y1):  
        print(max(X1,X2,X3),max(Y1,Y2,Y3))
    #x2,y2이 좌측 상단인 경우
    elif(min(X1,X2,X3)==X1 and max(Y1,Y2,Y3)==Y1):  
        print(max(X1,X2,X3),min(Y1,Y2,Y3))
    #x2,y2이 우측 상단인 경우
    elif(max(X1,X2,X3)==X1 and max(Y1,Y2,Y3)==Y1):  
        print(min(X1,X2,X3),min(Y1,Y2,Y3))
    #x2,y2이 우측 하단인 경우
    else:
        print(min(X1,X2,X3),max(Y1,Y2,Y3))


