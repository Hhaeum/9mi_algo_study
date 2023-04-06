# 섬의 개수 문제와 유사
# dfs로 붙어있는 땅덩어리가 몇 개인지 조사하시오.
import sys
sys.stdin = open('input.txt')


def dfs(i,j):
    stack= [] #스택에 시작점 넣어주기
    stack.append((i,j))
    visited[i][j] = 1
    while stack: #스택이 남아있는 동안
        ci,cj = stack.pop() #현재 위치
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]: # 상하좌우 탐색
            ni = di + ci
            nj = dj + cj
            if 0<= ni < N and 0<= nj <M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                stack.append((ni,nj))
                visited[ni][nj] = 1
    return

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        i, j = map(int,input().split())
        arr[j][i] = 1
    cnt = 0
    visited = [[0]*M for _ in range(N)] # 방문한 곳은 다시가지 말도록 방문한 곳 표시
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not visited[i][j]: # 배추 있는 곳에서 시작 근데 안 들렀어
                dfs(i,j) #dfs돌리고
                cnt += 1 # 땅덩어리 넓이
    print(cnt)



