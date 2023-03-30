# abcdefgh : 열 12345678

col = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # 'A'~'H' 열

move = {'R':(0, 1), 'L':(0, -1), 'B' : (1, 0), 'T': (-1, 0), 'RT':(-1,1), 'LT':(-1,-1), 'RB':(1,1), 'LB':(1,-1)}
# 움직일 수 있는 경우의수 8가지

board = [[0]*9 for _ in range(9)] # 보드, 0은 제외하고 1~8까지 사용

king, stone, N = input().split()

king_x, king_y = col.index(king[0]), 9 - int(king[1]) # X, Y 좌표를 받아줌. Y좌표 거꾸로.. 
stone_x, stone_y = col.index(stone[0]), 9 - int(stone[1]) 

for _ in range(int(N)):
    go = input()
    dy, dx = move[go]
    ny, nx = king_y + dy, king_x + dx 
    if 0 < ny < 9 and 0 < nx < 9: # 우선 가능한지
        if stone_y == ny and stone_x == nx: # stone이 있는지
            if 0 < stone_x+dx < 9 and 0 < stone_y+dy < 9: # stone의 영역이 가능한지
                stone_y += dy
                stone_x += dx
            else: 
                continue # stone 영역 불가능이면 둘다 움직이지 않아야 함
        king_y = ny
        king_x = nx


print(f'{col[king_x]}{9 - king_y}\n{col[stone_x]}{9 - stone_y} ') # 출력
