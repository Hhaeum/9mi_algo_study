

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    stickers = [list(map(int,input().split())) for _ in range(2)]

#     스티커의 누적합을 구해주기, 상하좌우가 안되니까 대각선+ 그 앞칸 열까지 고려하면 된다
#     일단 0열은 그대로, 1열의 경우 무조건 내 앞 대각선 값 더해주면 됨.
    for i in range(1, N):
        if i == 1:
            stickers[0][i] += stickers[1][0]
            stickers[1][i] += stickers[0][0]
        else:
            stickers[0][i] += max(stickers[1][i-1],stickers[1][i-2])
            stickers[1][i] += max(stickers[0][i-1],stickers[0][i-2])
# 반복문 다 돌면 마지막 열에 누적합이 나와있을 것임.
    print(max(stickers[0][N-1],stickers[1][N-1]))
