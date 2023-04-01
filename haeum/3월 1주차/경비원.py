W, H = map(int, input().split())
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())

cnt = 0

while arr:
    nr, nc = arr.pop(0)
    if r == 1:
        if nr == 3:
            cnt += (c + nc)
        elif nr == 4:
            cnt += (W - c + nc)
        elif nr == 2:
            a = H + c + nc
            b = H - nc + 2 * W - c
            cnt += min(a, b)
        else:
            cnt += abs(nc - c)

    if r == 2:
        if nr == 3:
            cnt += (c + H - nc)
        elif nr == 4:
            cnt += (W - c + H - nc)
        elif nr == 1:
            a = H + c + nc
            b = H - nc + 2 * W - c
            cnt += min(a, b)
        else:
            cnt += abs(nc - c)
    if r == 3:
        if nr == 1:
            cnt += (c + nc)
        elif nr == 2:
            cnt += (H - c + nc)
        elif nr == 4:
            a = W + c + nc
            b = 2 * H - c + W - nc
            cnt += min(a, b)
        else:
            cnt += abs(nc - c)
    if r == 4:
        if nr == 1:
            cnt += (W - nc + c)
        elif nr == 2:
            cnt += (W - nc + H - c)
        elif nr == 3:
            a = W + c + nc
            b = 2 * H - c + W - nc
            cnt += min(a, b)
        else:
            cnt += abs(nc - c)

print(cnt)