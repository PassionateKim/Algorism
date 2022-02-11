#별 찍기 - 10

# def get_stars(n):
#     matrix = []
#     for i in range(3 * len(n)):
#         if i // len(n) == 1:
#             matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
#         else:
#             matrix.append(n[i % len(n)] * 3)
#     return matrix
 
 
# star = ["***", "* *", "***"]
# n = int(input())
# e = 0
# while n != 3:
#     n = int(n / 3)
#     e+= 1
 
# for i in range(e):
#     star = get_stars(star)
# for i in star:
#     print(i)

star = ["***","* *","***"]

star2 = [star[0]*3,star[1]*3,star[2]*3
        ,star[0]+" "*3+star[0],star[1]+" "*3+star[1],star[2]+" "*3+star[2]
        ,star[0]*3,star[1]*3,star[2]*3]

star3 = [star2[0]*3,star2[1]*3,star2[2]*3,star2[3]*3,star2[4]*3,star2[5]*3,star2[6]*3,star2[7]*3,star2[8]*3
        ,star2[0]+" "*9+star2[0],star2[1]+" "*9+star2[1],star2[2]+" "*9+star2[2],star2[3]+" "*9+star2[3],star2[4]+" "*9+star2[4],star2[5]+" "*9+star2[5],star2[6]+" "*9+star2[6],star2[7]+" "*9+star2[7],star2[8]+" "*9+star2[8]
        ,star2[0]*3,star2[1]*3,star2[2]*3,star2[3]*3,star2[4]*3,star2[5]*3,star2[6]*3,star2[7]*3,star2[8]*3]
        
for i in star:
    print(i)

print("---------------------")
for i in star2:
    print(i)

print("---------------------")
for i in star3:
    print(i)

    