from collections import deque

def BFS():
    q = deque([(0, 0)])
    visited = [[0]*M for _ in range(N)]
    while q:
        y, x= q.popleft()
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            if 0<= ny < N and 0<= nx < M and visited[ny][nx] == 0 and miro[ny][nx] == '1':
                if ny == N-1 and nx == M-1:
                    return visited[y][x] + 2
                q.append((ny, nx))
                visited[ny][nx] += visited[y][x] + 1


N, M = map(int, input().split())

miro = [input() for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print(BFS())