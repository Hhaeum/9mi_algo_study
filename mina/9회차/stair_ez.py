# dp 써서 풀면 됨.. 아니면 시간 걸리더라
# 음.. 1씩 다 할당해서
# 음... N자리 까지 만들고..
# 시작할 숫자 양 옆, N-1 행 숫자 를 더하면 된다.....
# 9랑 0은 유의해 줘야 함..

N = int(input())

dp = [[1]*10 for _ in range(N)]

for i in range(1,N):
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][9] = dp[i-1][8]
    dp[i][0] = dp[i-1][1]

print(sum(dp[N-1][1:])%1000000000)