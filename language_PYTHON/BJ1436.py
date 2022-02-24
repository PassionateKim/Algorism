#영화감독 숌

from tabnanny import check

end_num = []

N = int(input())
n = 0
a = 666
while n < N:
    check_num = list(map(int,str(a)))
    
    reversed_num = list(reversed(check_num))
    
    x =0
    for i in reversed_num:
        if(i == 6):
            x += 1
            
        elif(i != 6):
            x = 0        
        if(x == 3):
            end_num.append(a)
            n += 1   
    a += 1
print(end_num[-1])
