N, r, c = map(int, input().split())

cnt = 0

while N > 0:
    # 범위를 좁힌다.
    N -= 1
    # print(r, c)
    # 맨 위 가장 작은 사각형 기준으로 1사분면부터 0, 1, 2, 3
    if r < 2 ** N <= c:
        cnt += (2 ** N) * (2 ** N)
        c -= (2 ** N)

    elif r >= 2 ** N > c:
        cnt += (2 ** N) * (2 ** N) * 2
        r -= (2 ** N)

    elif r >= 2 ** N and c >= 2 ** N:
        cnt += (2 ** N) * (2 ** N) * 3
        r -= (2 ** N)
        c -= (2 ** N)

print(cnt)