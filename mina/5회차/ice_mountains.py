from collections import deque

N, M = map(int, input().split()) # 행, 열

visited= [[0]*M for i in range(N)]

ice = [list(map(int, input().split())) for _ in range(N)]

year = 0
cnt = 0
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(year):
    while queue:
        y, x = queue.popleft()
        for dy, dx in dir:
            ny,  nx = dy+y, dx+x
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] < year:
                if ice[ny][nx] > 0:
                    visited[ny][nx] = year
                    queue.append((ny,nx))
                else:
                    ice[y][x] -= 1
    return 1


while True:
    cnt = 0
    year += 1
    for y in range(N):
        for x in range(M):
            if ice[y][x] > 0 and visited[y][x] < year:
                visited[y][x] = year
                queue = deque([(y, x)])
                cnt += BFS(year)    
    if cnt >= 2:
        break
    elif cnt == 0:
        year = 1
        break

print(year - 1)

