n = [0]*12
n[1] = 1
n[2] = 2
n[3] = 4
for i in range(4, 12):
    n[i]=n[i-1]+n[i-2]+n[i-3]

T = int(input())
for tc in range(T):
    print(n[int(input())])