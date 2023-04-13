# dfs로 풀면 될 거 같다.

# 단지 수/ 단지에 속하는 집의 갯수 (오름차순)

def dfs(i,j):
    stack = []
    house_cnt = 1
    stack.append((i,j))
    visited[i][j] = 1
    while stack:
        ci,cj = stack.pop()
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]: # 상하좌우
            ni = ci + di
            nj = cj + dj
            if 0<=ni<N and 0<=nj<N and board[ni][nj] and not visited[ni][nj]:
                stack.append((ni,nj))
                visited[ni][nj] = 1
                house_cnt += 1
    return house_cnt

N = int(input())
board = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
danji_cnt = 0
house_lst = []
for i in range(N):
    for j in range(N):
        if board[i][j]==1 and not visited[i][j]:
            house_lst.append(dfs(i,j))
            danji_cnt += 1
print(danji_cnt)
house_lst.sort()
for row in house_lst:
    print(row)