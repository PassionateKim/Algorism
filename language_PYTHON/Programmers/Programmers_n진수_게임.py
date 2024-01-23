def number_converter(number, jinsu):
    if number == 0:
        return '0'

    string = ''
    while number:

        tmp = number % jinsu
        if(tmp == 10):
            tmp = 'A'
        
        if(tmp == 11):
            tmp = 'B'
        
        if (tmp == 12):
            tmp = 'C'
        
        if(tmp == 13):
            tmp = 'D'
        
        if(tmp == 14):
            tmp = 'E'
        
        if(tmp == 15):
            tmp = 'F'

        string = str(tmp) + string

        number = number // jinsu

    return string



def solution(n, t, m, p):
    answer = []
    target_number = 0
    sequence = 1

    p = p % m

    while True:
        string = number_converter(target_number, n)

        for s in string:
            if (sequence % m) == p:
                answer.append(s)
            
            sequence += 1

            if(len(answer) == t):
                return "".join(answer)
        
        target_number += 1


solution(2, 4, 2, 1)