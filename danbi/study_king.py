def move_king(k, d, direction):
    global king, doll
    dir = move[direction]
    c = k[0]
    r = k[1]
    nr = r + dir[0]
    nc = c + dir[1]
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        if nr == doll[1] and nc == doll[0]:
            if 1 <= (doll[0] + dir[1]) <= 8 and 1 <= (doll[1] + dir[0]) <= 8:
                doll[0] = doll[0] + dir[1]
                doll[1] = doll[1] + dir[0]
            else:
                return
        king[0] = nc
        king[1] = nr
    return

# r, c
move = {
    'R':(0, 1),
    'L':(0, -1),
    'B':(-1, 0),
    'T':(1, 0),
    'RT':(1, 1),
    'LT':(1, -1),
    'RB':(-1, 1),
    'LB':(-1, -1),
}

alpabet_num = {
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8
}

num_alpabet = {
    '1':'A',
    '2':'B',
    '3':'C',
    '4':'D',
    '5':'E',
    '6':'F',
    '7':'G',
    '8':'H'
}

king, doll, N = input().split()
board = [[0]*8 for _ in range(8)]
king = list(king)
doll = list(doll)
N = int(N)
king[0] = alpabet_num[king[0]]
doll[0] = alpabet_num[doll[0]]
king = list(map(int, king))
doll = list(map(int, doll))
for _ in range(N):
    direction = input()
    move_king(king, doll, direction)
new_king = [num_alpabet[str(king[0])], str(king[1])]
new_doll = [num_alpabet[str(doll[0])], str(doll[1])]
new_king = "".join(new_king)
new_doll = "".join(new_doll)
print(new_king)
print(new_doll)

