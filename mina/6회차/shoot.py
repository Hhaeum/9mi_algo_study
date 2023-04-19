dir = [(1, 0),(-1, 0), (0, 1), (0, -1)]

def find_front():
    cnt = 0
    target = [0] * N
    for y in range(N):
        for x in range(N):
            if board[y][x]:
                target[y] = x
                cnt +=1
                break
    return target
    

def update_point(y, x, score):
    change = [0] * 4
    for i in range(4):
        ny, nx = y+dir[i][0], x+dir[i][1]
        if 0<=ny<N and 0<=nx<N and not board[ny][nx]:
            board[ny][nx] = score//4
            change[i] = 1
    return change


def restore(y, x, change):
    for i in range(4):
        if change[i]:
            ny, nx = y+dir[i][0], x+dir[i][1]
            board[ny][nx] = 0



def shoot(k, total):
    global ans
    target = find_front()
    if k == K: 
        ans = max(ans, total) 
        return 
    for i in range(N):  
        y, x = i, target[i] 
        score = board[y][x] 
        if score >= 10: 
            board[y][x] = 0 
            shoot(k + 1, total + score)  
            board[y][x] = score 
        
        elif 0 < score < 10: 
            memory[y] = max(memory[y], score) 
            board[y][x] -= bullet[k] 
            if board[y][x] <= 0:
                board[y][x] = 0
                tmp, memory[y] = memory[y], 0 
                if tmp//4 >= 1: 
                    change = update_point(y, x, tmp) 
                    shoot(k+1, total + tmp)
                    restore(y, x, change) 
                else:
                    shoot(k+1, total + tmp)
                memory[y] = tmp 
            else:
                shoot(k+1, total) 
            board[y][x] = score 


N = int(input()) # board 크기
K = int(input()) # 횟수
board = [list(map(int, input().split())) for _ in range(N)]
bullet = list(map(int, input().split()))
memory = [0]*N
ans = 0
shoot(0, 0)
print(ans)
