N = int(input())
answer = []

for i in range(1, N + 1):
    check_string = str(i)
    tmp = []
    is_clab = False
    for string in check_string:
        if string == '3' or string == '6' or string == '9':
            tmp.append('-')
            is_clab = True
    
    if is_clab:
        answer.append("".join(tmp))
    else:
        answer.append(check_string)

print(*answer)