#네 번째 점
X1, Y1 = map(int,input().split())
X2, Y2 = map(int,input().split())
X3, Y3 = map(int,input().split())


print(X1,Y1)
print(X2,Y2)
print(X3,Y3)

#총 case 6 개 

#min?


if((min(abs((X1-X2)**2+(Y1-Y2)**2),abs((X1-X3)**2+(Y1-Y3)**2),abs((X2-X3)**2+(Y2-Y3)**2)))==abs((X1-X2)**2+(Y1-Y2)**2)):
    print(X1,Y1,X2,Y2)

