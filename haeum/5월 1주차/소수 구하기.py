M, N = map(int, input().split())

for i in range(M, N + 1):   # N "이하"라서 N 포함
    if i != 1:
        tmp = int(i ** 0.5)  # 제곱해서 i가 나오는 수까지 검사
        # 이 때 소수부는 모두 버려도 상관 없으니까 int만 씌운다.
        for j in range(2, tmp + 1):
            if not i % j:
                break
        else:
            print(i)

