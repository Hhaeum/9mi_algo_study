T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    checked = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(K):
        X, Y = map(int, input().split())
        board[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if checked[i][j] == 0 and board[i][j] == 1:
                stack = []
                stack.append((i, j))
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr = cr + dr
                        nc = cc + dc
                        if 0 <= nr < N and 0 <= nc < M and checked[nr][nc] == 0 and board[nr][nc] == 1:
                            checked[nr][nc] = 1
                            stack.append((nr, nc))

                cnt += 1
    print(cnt)
