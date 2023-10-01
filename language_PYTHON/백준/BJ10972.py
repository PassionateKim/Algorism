import sys
input = sys.stdin.readline

n = int(input())
perm = list(map(int, input().split()))

# 맨 뒤부터 탐색
for i in range(n-1, 0, -1):
    # 뒷 값이 앞 값보다 크면
    if perm[i-1] < perm[i]:
        # 다시 뒤에서부터, 앞 값보다 큰 값이 있는지 탐색
        for j in range(n-1, 0, -1):
            # 뒷 값이 앞 값보다 크면
            if perm[i-1] < perm[j]:
                # 두 값을 swap
                perm[i-1], perm[j] = perm[j], perm[i-1]
                # 뒷 값의 인덱스부터 끝까지 오름차순 정렬 후 출력
                perm = perm[:i] + sorted(perm[i:])
                print(" ".join(map(str, perm)))
                exit()
# 만약 뒷 값이 앞 값보다 큰 경우가 없다면, 맨 마지막 순열이므로 -1
print(-1)

# import sys
# si = sys.stdin.readline 
# N = int(si())
# target_list = list(map(int, si().split()))
# remember = target_list[:]

# for i in range(len(target_list) -1, 0, -1):
#     check_target_index = -1
#     if target_list[i-1] < target_list[i]:
#         check_target_index = i-1
#     if check_target_index != -1:
#         first_bigger_index = 0
#         for j in range(len(target_list)-1 , check_target_index, -1):
#             if target_list[j] > target_list[check_target_index]:
#                 # swap 해야함
#                 tmp = target_list[check_target_index]
#                 target_list[check_target_index] = target_list[j]
#                 target_list[j] = tmp
#                 break
#         if j == len(target_list) - 1:
#             target_list = target_list[:i] + sorted(target_list[j:])
#         else:
#             target_list = target_list[:i] + sorted(target_list[j-1:])
#         break

# if remember == target_list:
#     print(-1)
# else:
#     print(*target_list)