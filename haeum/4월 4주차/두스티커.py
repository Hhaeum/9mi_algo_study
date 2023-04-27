def check(A, B):
    global ans
    if A[0] + B[0] <= H:
        if max(A[1], B[1]) <= W:  # 붙일 수 있음!
            ans = max(ans, (A[0]*A[1] + B[0]*B[1]))
            return True

    if A[0] + B[0] <= W:
        if max(A[1], B[1]) <= H:  # 붙일 수 있음!
            ans = max(ans, (A[0]*A[1] + B[0]*B[1]))
            return True
    return False

def doubleCheck(A, B):
    if check(A, B):
        return
    if check(A, B[1:: -1]):
        return
    if check(A[1:: -1], B):
        return
    check(A[1:: -1], B[1:: -1])

H, W = map(int, input().split())
N = int(input())
stickers = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N - 1):
    A_sticker = stickers[i]
    for j in range(i + 1, N):
        B_sticker = stickers[j]
        doubleCheck(A_sticker, B_sticker)

print(ans)