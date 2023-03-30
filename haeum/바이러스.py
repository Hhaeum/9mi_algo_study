N = int(input())
C = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
Ca = [list(map(int, input().split())) for _ in range(C)]
for a, b in Ca:
    arr[a][b], arr[b][a] = 1, 1
go = []
check = [0] * (N + 1)
check[1] = 1
for j in range(2, N + 1):
    if arr[1][j]:
        go.append(j)

while go:
    i = go.pop()
    if check[i]:    # 가지치기
        continue
    check[i] = 1
    for j in range(2, N + 1):
        if check[j]:    # 와본적 있으면 pass
            continue
        if arr[i][j]:
            go.append(j)
cnt = -1
for i in range(N + 1):
    if check[i]:
        cnt += 1

print(cnt)