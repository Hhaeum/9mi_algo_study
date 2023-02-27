sugar = int(input())
N = 0
while sugar >=0 :
    if not sugar//15 and not sugar % 3:
        N += sugar//3
        sugar = 0
        break
    sugar -= 5
    N += 1

if sugar < 0 :
    N = -1
print(N)