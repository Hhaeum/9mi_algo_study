def bfs(x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = dr + x
            nc = dc + y
            if 0 <= nr < M and 0 <= nc < N:
                if field[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)]
    # [X][Y] -> [M][N]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[X][Y] = 1
        # 배추 심기
    visited = [[0] * N for _ in range(M)]
    cnt = 0


    for i in range(M):
        for j in range(N):
            if field[i][j] and not visited[i][j]:
                # 여기서 bfs 돌면서 배추 다 방문하기
                visited[i][j] = 1
                bfs(i, j)
                cnt += 1

    print(cnt)