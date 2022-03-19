# #회의실 배정
# import sys
# N = int(input())
# convention = []

# for i in range(N):
#     convention.append(list(map(int,sys.stdin.readline().rstrip().split())))

# convention.sort(key= lambda x:(x[1],x[0]))

# cnt = 1
# end_convention = convention[0][1]

# for i in range(1,N):
#     if convention[i][0] >= end_convention:
#         cnt += 1
#         end_convention = convention[i][1]

# print(cnt)








import sys
N = int(input())
convention=[]
for i in range(N):
    convention.append(list(map(int,sys.stdin.readline().rstrip().split())))

convention.sort(key=lambda x:(x[1],x[0]))

cnt = 1 
values = []
values.append(convention[0])
end_convention = convention[0][1]
for i in range(N):
    if(convention[i][0] >= end_convention):
        cnt += 1
        end_convention = convention[i][1]
        values.append(convention[i])

print(cnt,values)

