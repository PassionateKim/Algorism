#오큰수
N = int(input())
arr = list(map(int,input().split()))
result = [-1] * N
stack = [0]

for i in range(1,N):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)


#기존풀이
# N = int(input())
# answer = []
# su_yeol = list(map(int,input().split()))

# for i in range(len(su_yeol)):
#     flag = 0
#     for j in range(len(su_yeol)):
#         #중복제거
#         if(i<j):
#             if(su_yeol[i] < su_yeol[j]):
#                 answer.append(su_yeol[j])
#                 flag = 1
#                 break
#             elif(j == len(su_yeol) - 1 and flag == 0):
#                 answer.append(-1)
# answer.append(-1)

# for i in answer:
#     print(i,end=" ")