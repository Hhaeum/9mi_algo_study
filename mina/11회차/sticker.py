T = int(input()) # 테스트케이스 개수
for tc in range(T):
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    # 여기까지 입력

    dp = [[0]*(N+1) for _ in range(2)] # dp 배열 생성

    dp[0][1], dp[1][1] = sticker[0][0], sticker[1][0]
    # 0번과 1번 행은 직접 넣어 줌.
    # 그 이후부터는 지금 행의 전 대각선, 전전 대각선 중 큰걸 찾아서 더하면 된다.
    for i in range(2,N+1):
        for j in range(2):
            now = sticker[j][i-1]
            pre = (j+1)%2
            dp[j][i] = max(dp[pre][i-1], dp[pre][i-2]) + now

    print(max(dp[0][N], dp[1][N]))

