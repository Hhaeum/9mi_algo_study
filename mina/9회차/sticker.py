
H, W = map(int, input().split())
max_v = max(H,W)
min_v = min(H,W)

N = int(input())

sticker = list()

for i in range(N):
    a, b = map(int, input().split())
    sticker.append((a*b, a, b))

sticker.sort() # 백트래킹 할 생각으로 정렬했는데 그냥 되더라 ㅇㅅㅇ

max_w = 0
# print(sticker)
for i in range(N-1, 0 ,-1):
    # 큰거 선택
    r, c = sticker[i][1], sticker[i][2]
    for j in range(i-1, -1, -1):
        # 작은거 선택
        nr, nc = sticker[j][1], sticker[j][2]
        # 갖다 붙는 4가지 경우가 있음.
        # 백트래킹으로 한 거 보다 적은 면적 없앨 수 있는데 그냥 함.
        check = [(r + nr, max(c, nc)), (c + nc, max(r, nr)), (r + nc, max(c, nr)), (c + nr, max(r, nc)) ]
        for l, s in check:
            if (l <=H and s <= W) or (l <= W and s<=H):
                max_w = max(max_w, sticker[i][0]+sticker[j][0] )
                break
print(max_w)

