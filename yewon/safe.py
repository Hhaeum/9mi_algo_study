import sys
sys.stdin = open('input.txt')

# 안전영역은 한 덩어리로 보는 듯.
def dfs(si,sj,h): #하나하나 돌아보면서 높이를 비교해줘야 함.
    stack = []
    stack.append((si,sj))
    visited[si][sj] = 1
    while stack:
        ci,cj = stack.pop()
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = ci + di
            nj = cj + dj
            if 0<= ni < N and 0<= nj <N and visited[ni][nj] == 0 and arr[ni][nj]>h:
                stack.append((ni,nj))
                visited[ni][nj] = 1
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

max_v = -0xfffffff
for k in range(100): #최대 높이
    stack = []
    visited = [[0]*N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] > k:
                dfs(i, j, k)
                cnt += 1
    if max_v < cnt:
        max_v = cnt

print(max_v)
