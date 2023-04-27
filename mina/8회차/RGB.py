N = int(input())

RGB = [list(map(int, input().split())) for _ in range(N)]
pre = RGB[0]
now = [0]*3

for i in range(1,N): # RGB배열
    # print(pre)
    for j in range(3): # RGB[i] 배열 돌기
        min_v = float('inf')
        for k in range(3): # pre 배열 돌기
            if j != k:
                min_v = min(min_v, pre[k]+RGB[i][j])
        now[j] = min_v
    pre = now[:]

print(min(pre))
