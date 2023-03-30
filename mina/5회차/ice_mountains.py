from collections import deque

N, M = map(int, input().split()) # 행, 열

visited= [[0]*M for i in range(N)] # 방문한 전적

ice = [list(map(int, input().split())) for _ in range(N)]

year = 0
cnt = 0
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(year): # bfs로 빙산의 덩어리를 찾아준다.
    while queue: # queue가 비면 끝
        y, x = queue.popleft() 
        for dy, dx in dir:
            ny,  nx = dy+y, dx+x
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] < year: # 올 해 확인한 게 아니면
                if ice[ny][nx] > 0: # 0보다 크면 올해 방문했다고 남겨주고
                    visited[ny][nx] = year
                    queue.append((ny,nx)) # bfs에도 넣어줌
                else:
                    ice[y][x] -= 1 # 0보다 작으면 == 물이다. 현재 빙하를 녹여준다.
    return 1


while True:
    cnt = 0
    year += 1
    for y in range(N):
        for x in range(M):
            if ice[y][x] > 0 and visited[y][x] < year:
                visited[y][x] = year
                queue = deque([(y, x)]) # 찾은 곳에서
                cnt += BFS(year) # bfs 시작    
    if cnt >= 2: # 2이상이면 브레이끼
        break
    elif cnt == 0: # 다 녹아서 하나도 없으면 0을 출력해야 하므로 year = 1 
        year = 1
        break

print(year - 1)

