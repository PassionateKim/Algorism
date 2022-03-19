#잃어버린 괄호
formula = list(map(str,input().split('-')))

answer = 0
if '+' in formula[0]:
    a = list(map(int,formula[0].split('+')))
    answer = sum(a)
else:
    answer = int(formula[0]) 
for i in range(1,len(formula)):
    if '+' in formula[i]:
        counting = list(map(int,formula[i].split('+')))
        answer = answer - sum(counting)
    else:
        answer = answer - int(formula[i])

print(answer)
        

    
    
    