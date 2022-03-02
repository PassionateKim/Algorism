n = int(input())
 
li = []
for _ in range(n):
    li.append(int(input()))
 

# 최빈값 - 빈출
# 파이썬에 Counter함수가 있으나 사용하지않음
number = list(set(li)) # 중복제거
print(li)
print(number)
max_fre = []
max_cnt = 0
for i in number:
    print(i, li.count(i))
    if max_cnt == li.count(i):
        max_fre.append(i)
    elif max_cnt < li.count(i):
        max_fre = []
        max_fre.append(i)
        max_cnt = li.count(i)
if len(max_fre) > 1: # 최빈값이 2개이상
    max_fre.sort()
    print(max_fre[1])
else: # 최빈값 1개
    print(max_fre[0])