N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

for i in range(N): # 보려는 데이터
    cnt = 0
    for j in range(N): # 비교할 데이터
        if i != j and  data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    print(cnt + 1, end=' ')