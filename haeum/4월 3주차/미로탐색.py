def bfs():
    # 그림으로는 1, 1부터 시작이지만 인덱스로는 0, 0부터 시작
    # cnt에는 시작 칸도 포함한다.
    queue = [(0, 0, 1)]

    while queue:
        r, c, cnt = queue.pop(0)
        if r == N - 1 and c == M - 1:
            return cnt
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if maze[nr][nc] == '1' and not visited[nr][nc]:
                    queue.append((nr, nc, cnt + 1))
                    visited[nr][nc] = 1


N, M = map(int, input().split())
maze = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(bfs())