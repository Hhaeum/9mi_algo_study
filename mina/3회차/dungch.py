# 사람의 덩치 : 키, 몸무개
# 무조건 둘 다 큰 경우에만 큰 사람
# 정렬 
# 입력 받고
# 돌아가면서 센다. 

N = int(input())
arr = [0] * N
st = [1]*N
for i in range(N):
    y, x = map(int, input().split())
    arr[i] = (y, x)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            st[i] += 1

print(*st)