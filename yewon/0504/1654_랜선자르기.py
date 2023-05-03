K, N = map(int,input().split())
lan = [int(input()) for _ in range(K)]

start = 1
end = max(lan)

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for e in lan:
        cnt += e//mid
        # 랜선을 자른 수
    if cnt>=N:
        # 만약 개수가 N보다 크면 -> 더 큰 수로 잘라
        start = mid + 1
    else:
        end = mid -1
print(end)

