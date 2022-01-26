num = int(input())
i = 2
if(num == 1):
    print('')
else:
    for i in range(i,num+1):
        if(num%i) == 0:
         while num%i == 0:
                print(i)
                num = num/i
