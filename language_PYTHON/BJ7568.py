#덩치

N = int(input())
frames = []
for i in range(1,N+1):
    a,b = map(int,input().split())
    frames.append([a,b])

for i in range(len(frames)):
    score = 1
    for j in range(len(frames)):
        if(i != j and frames[i][0]<frames[j][0] & frames[i][1]<frames[j][1]):
            score += 1
    print(score, end=" ")



                
        

