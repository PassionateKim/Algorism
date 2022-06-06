# 타겟 넘버

def dfs(depth, sum, nums, target):
    global answer
    
    if sum == target and depth == len(nums):
        answer += 1
        return
    elif depth == len(nums):
        return

    dfs(depth+1, sum - nums[depth] , nums, target)
    dfs(depth+1, sum + nums[depth] , nums, target)


    return


answer = 0

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    
    print(answer)
    return answer

solution([4, 1, 2, 1], 4)