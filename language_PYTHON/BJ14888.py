#연산자 끼워넣기
#+ - x ÷
N = int(input())
A_array = list(map(int,input().split()))
arithmetic_operations = list(map(int,input().split()))
answer = []

count = 0
def dfs(idx,sum,add,minus,multi,div):
    global count
    if(idx == N-1):
        answer.append(sum)
        return
    
    if(add):
        dfs(idx+1,sum+A_array[idx+1],add-1,minus,multi,div)
    
    if(minus):
        #계속 값이 이상했던 이유 -> minus에 minus-1 치환을 안해줬었음 실수 유형체크
        dfs(idx+1,sum-A_array[idx+1],add,minus-1,multi,div)
    
    if(multi):
        dfs(idx+1,sum*A_array[idx+1],add,minus,multi-1,div)
    
    if(div):
        #음수를 양수로 나눌 때는 C++14의 기준을 따른다.양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
        if(sum < 0):
            sum = abs(sum)
            sum = sum // A_array[idx+1]
            sum = -sum
        else:
            sum = sum // A_array[idx+1]
        dfs(idx+1,sum,add,minus,multi,div-1)


    
dfs(0,A_array[0],arithmetic_operations[0],arithmetic_operations[1],arithmetic_operations[2],arithmetic_operations[3])

print(max(answer))
print(min(answer))