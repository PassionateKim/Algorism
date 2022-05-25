# 소수 만들기
Prime_nums = [False, False] + [True] * (3000)

for i in range(2, len(Prime_nums)):
    if Prime_nums[i]: 
        for j in range(i*i, len(Prime_nums), i):
            Prime_nums[j] = False
val_list = []

def dfs(depth, idx, nums):
    global answer
    if depth == 3:
        if Prime_nums[sum(val_list)]:
            answer += 1
        return        

    for i in range(idx, len(nums)):
            if nums[i] not in val_list:
                val_list.append(nums[i])
                dfs(depth+1, i, nums)
                val_list.pop()
answer = 0
def solution(nums):
    dfs(0, 0, nums)

    return answer

print(solution([1,2,7,6,4]))