# 좋은수열
N = int(input())
suyeol_list = [1,2,1,3,1,2,1]
print(suyeol_list[-2:0])
# def isGoodArr(arr): #1213121
#     arr_len = len(arr) # 7
#     for part_len in range(1, arr_len//2 + 1): # 개수시작# 1, 2, 3
#         # 부분수열 비교 시작
#         for part_start in range(part_len, arr_len - part_len + 1): # 1 6
#             if arr[part_start-part_len:part_start] == arr[part_start:part_start+part_len]:
#                 return False
#     return True



# def dfs(depth):
#     if depth == N:
#         print("".join(list(map(str, suyeol_list)))) # 수열 출력
#         exit()
    
    
#     for i in range(1, 4):
#         suyeol_list.append(i)
#         if isGoodArr(suyeol_list):
#             dfs(depth+1)
#         suyeol_list.pop()

# dfs(0)