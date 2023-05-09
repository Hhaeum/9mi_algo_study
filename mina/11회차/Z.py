def find_num(ans, N, r, c):
    if N==1:
        print(ans + r*2 + c)
        return ans + r * 2 + c

    if r >= 2**(N-1):
        r -= 2**(N-1)
        ans += 2 ** (2 * N - 1)

    if c >= 2**(N-1):
        c -= 2**(N-1)
        ans += 2 ** (2*N - 2)
    find_num(ans, N-1, r, c)

N, r, c = map(int, input().split())
find_num(0, N, r, c)