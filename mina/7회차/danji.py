

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def set_num(y, x, cnt): # 음.. 그냥 BFS
    q = [(y, x)]
    visited[y][x] = cnt
    home_cnt = 0
    while q:
        y, x = q.pop(0)
        home_cnt += 1
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            if 0<= ny< N and 0<= nx< N and apartment[ny][nx] =='1' and visited[ny][nx] == 0:
                visited[ny][nx] = cnt
                q.append((ny, nx))
    ans.append(home_cnt) # 답을 넣어줌..


    
N = int(input())
apartment = [input() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
ans = []
cnt = 0

for y in range(N):
    for x in range(N):
        if apartment[y][x] == '1' and visited[y][x] == 0:
            cnt += 1
            set_num(y, x, cnt)
             
ans.sort() #정렬도 하래...
print(cnt) 
for i in ans:
    print(i)