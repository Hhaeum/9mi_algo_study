from collections import deque

def BFS(y, x):
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            if 0 <= ny< N and 0<= nx < M and visited[ny][nx] == 0 and farm[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = 1

    return 1



dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]



T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*M  for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for y in range(N):
        for x in range(M):
            if farm[y][x] == 1 and visited[y][x] == 0:
                cnt += BFS(y, x)

    print(cnt)