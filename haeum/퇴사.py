N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)
for i in range(N-1, -1, -1): # 모든 날을 끝에서부터 순회
    date = arr[i][0]
    pay = arr[i][1]
    if date + i <= N : # 만약 현재 날과 소요 일자가 N보다 작다면
        dp[i] = max(pay + dp[date + i], dp[i + 1])
        # 오늘 일을 하면 vs 그냥 내일 하면
    else:
        dp[i] = dp[i + 1]
        # 만약 현재 날 + 소요 시간이 남은 날보다 길면 이 전까지 받은 돈이 들어감 못벌어 이날은
print(dp[0])