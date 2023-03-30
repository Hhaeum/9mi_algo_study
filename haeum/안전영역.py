import sys
sys.setrecursionlimit(100000)
def search(i, j, k):
    if 0 <= j < N and 0 <= k < N:
        if arr[j][k] > i and not visited[j][k]:
            visited[j][k] = 1
            # 하나의 안전지대라면 visited에 표시해서 다시 안오기 위함...
            search(i, j - 1, k)
            search(i, j + 1, k)
            search(i, j, k - 1)
            search(i, j, k + 1)
            return True
    return False

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_cnt = 0
max_v = 0
min_v = 0xffffff

for i in range(N):
    if max(arr[i]) > max_v:
        max_v = max(arr[i]) # 지대의 최대 높이
    if min(arr[i]) < min_v:
        min_v = min(arr[i]) # 지대의 최소 높이

for i in range(min_v - 1, max_v + 1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if search(i, j, k):
                cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)

