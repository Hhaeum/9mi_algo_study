def search_land():
    while stack:                        # stack이 빌 때 까지 계속 반복 (DFS)
        y, x = stack[-1]                # y, x는 stack의 젤 위
        for dy, dx in dir:              # 8방향 탐색
            ny, nx = y + dy, x + dx  
            if -1 < nx < N and -1 < ny < M and land[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = 1     # 방문 전적을 1로 바꿔주고
                stack.append((ny, nx))  # stack에 넣어준다.
                break
        else:
            stack.pop()                 # 8방향 탐색이 모두 진행되면 갈 수 있는 방향이 없음으로 판단 => 그 전의 길에서 다시 탐색


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    land = [list(map(int, input().split())) for _ in range(M)]
    cnt = 0
    visited = [[0] * N for _ in range(M)]
    stack = []
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for y in range(M):
        for x in range(N):
            if land[y][x] == 1 and not visited[y][x]:
                cnt += 1                # 섬의 시작인 1을 만나면 cnt 개수를 늘려준다.
                visited[y][x] = 1
                stack.append((y, x))    # stack에 넣어줌.
                search_land()
    print(cnt)