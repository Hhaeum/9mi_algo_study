import sys
sys.stdin = open('input.txt')

def dfs(si,sj):

    while stack:
        ci, cj = stack.pop()
        for di,dj in [(1,-1),(1,0),(1,1),(0,-1),(0,1),(-1,-1),(-1,0),(-1,1)]:
            ni = ci + di
            nj = cj + dj
            if 0<=ni<H and 0<=nj<W and board[ni][nj] and not visited[ni][nj]:
                stack.append((ni,nj))
                visited[ni][nj] = 1





while True:
    W, H = map(int,input().split())
    if W == 0 and H == 0:
        break
    board = [list(map(int,input().split())) for _ in range(H)]
    cnt = 0

    visited = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if board[i][j] and not visited[i][j]:#1이면 섬
                stack = [(i, j)]
                visited[i][j] = 1
                dfs(i,j)
                cnt += 1
    print(cnt)


