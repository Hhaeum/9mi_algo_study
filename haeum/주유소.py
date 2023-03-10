N = int(input())
arr = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost.pop(-1)
min_idx = [cost.index(min(cost))]
ans = 0
while min_idx[-1] > 0:
    min_idx.append(cost.index(min(cost[:min_idx[-1]])))
nc = min_idx.pop(-1)
while min_idx:
    c = min_idx.pop(-1)
    for i in range(nc, c):
        ans += arr[i]*cost[nc]
    nc = c
for i in range(nc, N - 1):
    ans += arr[i]*cost[nc]

print(ans)