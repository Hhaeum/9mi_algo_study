def check(num):
    now = [0]*K
    for i in range(K):
        now[i] = line[i] //num
    return sum(now)

def find(start, end):
    if start > end:
        return
    mid = (start + end) // 2
    now = check(mid)
    if now >= N:
        if now == N:
            ans.append(mid)
        find(mid+1, end)
    else:
        find(start, mid-1)

K, N = map(int, input().split())
line = [0]*K
for i in range(K):
    line[i] = int(input())

max_v = max(line)
ans = []
find(1, max_v)

print(max(ans))



