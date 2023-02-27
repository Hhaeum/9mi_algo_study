def dfs(si, sj):
    global cnt
    stack = []
    stack.append((si, sj))
    visited[si][sj] = 1

    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    while stack:
        ci, cj = stack[-1]
        for m in range(8):
            ni = ci + di[m]
            nj = cj + dj[m]

            if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == 0 and world[ni][nj] == 1:
                stack.append((ni, nj))
                visited[ni][nj] = 1
                break
        else:
            stack.pop()
    cnt += 1
    return

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    world = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    visited = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if world[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)

    print(cnt)
