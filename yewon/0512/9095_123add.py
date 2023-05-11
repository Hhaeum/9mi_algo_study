T= int(input())
for tc in range(T):
    N = int(input())
    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    # 여기까지는 값 직접 넣어줘야 함.
    # i번째의 개수 구하기
    for i in range(4,11):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N])