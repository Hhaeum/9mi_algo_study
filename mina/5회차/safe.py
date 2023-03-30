N = int(input())

visited = [[-1]*N for _ in range(N)]

home = [list(map(int, input().split())) for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

max_cnt = 0

def is_safe(n): # 안전한 영역인지 판별하는 BFS
    while queue: # BFS
        y, x = queue.pop(0)
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < N:
                if home[ny][nx] > n and visited[ny][nx] < n: 
                    visited[ny][nx] = n
                    queue.append((ny,nx))
    return 1

# 매번 갱신 되어야 함. 
# EX) 1만 잠겼을때, 2만 잠겼을 때,,,,
# 매번 visited를 생성할 순 없으니, 
# 침수 정도를 기준으로, 갱신을 해주고
# max 값을 바꿔줌

for n in range(0, 101): # 0~100 까지 살펴봄
    cnt = 0 # 땅 갯수 세기
    for y in range(N): # y 업
        for x in range(N): # x 업
            if n < home[y][x] and visited[y][x] < n: # 해당 집이 잠길 집인가? 이번 침수에서 확인해봤는가? 
                queue = [(y, x)] # 잠길 집이 아니고, 침수에서 확인 안해봤으면 queue에 넣고
                visited[y][x] = n # 안잠겼다고 표기도 해줌
                cnt += is_safe(n) # 영역 확인!

    if cnt == 0: # 만약, 남은 집이 하나도 없다면 그 이상 침수에서도 없을 거임
        break
    max_cnt = max(cnt, max_cnt)

print(max_cnt)
