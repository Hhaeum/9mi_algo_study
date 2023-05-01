K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
max_v = max(arr)
min_v = 1

while min_v <= max_v:
    mid = (max_v + min_v) // 2  # 이름이 mid긴 한데...
    tmp = [x // mid for x in arr]
    if sum(tmp) < N:    # 쪼개진 모든 랜선의 개수가 N보다 작으면
        max_v = mid - 1    # max_v 값 줄여서 재시도하기
    else:
        min_v = mid + 1
        ans = mid

print(ans)