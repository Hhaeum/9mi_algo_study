def bfs(i,j, cnt):
    queue = []
    queue.append((i,j,cnt))
    visited[i][j] = 1
    while queue:
        ci, cj, ccnt = queue.pop(0)
        if ci == N-1 and cj == M-1:
            return ccnt
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]: #상하좌우
            ni = ci + di
            nj = cj + dj
            if 0<= ni < N and 0<= nj < M and not visited[ni][nj] and maze[ni][nj]:
                queue.append((ni,nj, ccnt + 1))
                visited[ni][nj] = 1

N,M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]
# 1콤마 1에서 출발 -> 걍 0,0이라고 넣어도 됨
visited = [[0]*M for _ in range(N)]
print(bfs(0,0,1)) # 자기 첫자리 포함해야 해서 cnt값은 1로 시작!
