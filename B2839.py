# 섵탕 N 킬로그램 배달
# 최대한 적은 봉지
def delivery(N):
    # 최대한 5kg으로 만들 수 있는 만큼 만들자.
    mox = N // 5
    while mox >= 1:
        a = N - (5 * mox)
        if a % 3 == 0:
            b = a // 3
            return mox + b
        else:
            mox -= 1
    # 만약 다 돌았는데 답이 안 나오면 3으로 나눠보자
    if N % 3 == 0:
        b = N // 3
        return b
    # 그래도 안되면 -1 출력

    return -1

N = int(input())
print(delivery(N))
