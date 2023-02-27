import sys
sys.setrecursionlimit(10000)

def dfs(r, c):
    arr[r][c] = 0
    for dr, dc in direction:
        nr, nc = r + dr, c + dc
        if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1:
            dfs(nr, nc)

direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)