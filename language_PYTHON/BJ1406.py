import sys
st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
    
    elif command[0] == 'B':
        if st1:
            st1.pop()
    
    else: #P 
        st1.append(command[1])
    

st1.extend(reversed(st2))
print(''.join(st1))



# # 에디터
# import sys
# input = sys.stdin.readline

# char_array = list(map(str, input().rstrip()))
# cursor_location = [0 for _ in range(len(char_array))]
# cursor_location.append(1) # 시작지점은 끝임
# N = int(input())

# for i in range(N):
#     c = input().rstrip()

#     if "L" in c:
#         if cursor_location.index(1) == 0:
#             continue
#         tmp = cursor_location.index(1)
#         cursor_location[tmp] = 0
#         cursor_location[tmp - 1] = 1

#     elif "D" in c:
#         if cursor_location.index(1) == len(cursor_location) -1:
#             continue
#         tmp = cursor_location.index(1)
#         cursor_location[tmp] = 0
#         cursor_location[tmp + 1] = 1

#     elif "B" in c:
#         if cursor_location.index(1) == 0:
#             continue
#         tmp = cursor_location.index(1)
#         char_array.pop(tmp-1) # 시간 복잡도 O(N)
#         cursor_location.pop(0)
    
#     elif "P" in c:
#         tmp = cursor_location.index(1)
#         char_array.insert(tmp, c.split()[1])
#         cursor_location.insert(0,0)

# for i in char_array:
#     print(i,end='')