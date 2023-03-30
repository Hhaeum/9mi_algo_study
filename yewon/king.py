import sys
sys.stdin = open('input.txt')

king,dol,N = input().split()
move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}
dir = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
N = int(N)
king_r, king_c = dir[king[0]], int(king[1]),
dol_r,dol_c = dir[dol[0]], int(dol[1]) #돌의 첨 위치
for i in range(N):
    a = input()
    k_nr = king_r + move[a][0]
    k_nc = king_c + move[a][1]
    if 0< k_nr <= 8 and 0< k_nc <=8 : #범위 내
        if k_nr == dol_r and k_nc == dol_c:
            dol_nr = dol_r + move[a][0]
            dol_nc = dol_c + move[a][1]
            if 0< dol_nr <= 8 and 0< dol_nc <=8 :
                dol_r = dol_nr
                dol_c = dol_nc
                king_r = k_nr
                king_c = k_nc  # 이동
            else:
                continue
        else:
            king_r = k_nr
            king_c = k_nc  # 이동
r1 = [k for k,v in dir.items() if v == king_r ]
r2 = [k for k,v in dir.items() if v == dol_r ]
result1 = r1[0] + str(king_c)
result2 = r2[0] + str(dol_c)

print(result1)
print(result2)