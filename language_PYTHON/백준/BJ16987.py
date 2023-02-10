# 계란으로 계란치기
# 복습 횟수:0, 02:30:00, 복습필요O
import sys
input = sys.stdin.readline

def check(eggs):
  count = 0
  for egg in eggs:
    if egg[0] <= 0:
      count += 1
  return count

def dfs(index, eggs):
  global answer
  
  if index == n:
    answer = max(answer, check(eggs))
    return 

  if eggs[index][0] <= 0:
    # 현재 계란의 내구도가 다 달았을 때 다음 계란으로 넘어간다.
    dfs(index + 1, eggs)
  else:
    # 현재 계란의 내구도가 남아있을 때 다른 계란들과 부딪친다. (현재 계란 제외, 내구도가 없는 계란 제외)
    is_all_broken = True
    for i in range(len(eggs)):
      if index != i and eggs[i][0] > 0:
        is_all_broken = False
        eggs[index][0] -= eggs[i][-1]
        eggs[i][0] -= eggs[index][-1]
        dfs(index + 1, eggs)
        eggs[index][0] += eggs[i][-1]
        eggs[i][0] += eggs[index][-1]
    # 모든 계란이 깨져있는 경우 dfs를 바로 빠져나와준다.
    if is_all_broken:
      dfs(n, eggs)

n = int(input())
eggs = []
answer = 0
for _ in range(n):
  eggs.append(list(map(int, input().split())))

dfs(0, eggs)
print(answer)

# ====0 이하일 땐 체크를 안해도 되는데 내 풀이에서는 체크를 한다는게 문제====
# import sys
# si = sys.stdin.readline

# N = int(si())
# egg_list = []
# for i in range(N):
#     h, w = map(int, si().split())
#     egg_list.append([h, w, 1]) # 내구도, 무게, 상태 : 1은 정상

# answer = 0
# cc = 0
# def dfs(start, target):
#     global cc
#     cc += 1
#     global answer
#     if start == len(egg_list):
#         cnt = 0
#         for i in range(len(egg_list)):
#             if egg_list[i][2] <= 0:
#                 cnt += 1
#         answer = max(answer, cnt)
#         return

#     for i in range(len(egg_list)):
#         if (start + 1) == i: continue

#         if egg_list[start][2] > 0 and egg_list[target][2] > 0: 

#             # 아니라면 계산하기.
#             egg_list[start][0] -= egg_list[target][1]
#             egg_list[target][0] -= egg_list[start][1]

#             if egg_list[start][0] <= 0:
#                 if egg_list[target][0] <= 0:
#                     egg_list[start][2] = 0
#                     egg_list[target][2] = 0
#                     dfs(start+1, i)
#                     egg_list[start][2] = 1
#                     egg_list[target][2] = 1
                    
#                 else:
#                     egg_list[start][2] = 0
#                     dfs(start+1, i)
#                     egg_list[start][2] = 1
#             else: 
#                 if egg_list[target][0] <= 0:
#                     egg_list[target][2] = 0
#                     dfs(start+1, i)
#                     egg_list[target][2] = 1
#                 else:
#                     dfs(start+1, i)

#             egg_list[start][0] += egg_list[target][1]
#             egg_list[target][0] += egg_list[start][1]
#         else:
#             dfs(start+1, i)
    
#     return

# for i in range(1, len(egg_list)):
#     dfs(0, i)
# print(answer)
# print(cc)