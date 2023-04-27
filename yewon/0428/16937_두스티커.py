# 아이디어 : 브루트 포스로 모든 경우의 수 탐색
# 두 개씩 짝을 지어 모든 경우의 수를 탐색해서
# 범위를 넘는 것을 제외하고
# 둘의 넓이를 더했을 때 최댓값인 것을 출력한다.
H, W = map(int,input().split())
N = int(input())
sticker = [list(map(int,input().split())) for _ in range(N)]
max_monun = max(H,W)
for i in range(N):
    if sticker[i][0] > max_monun or sticker[i][1] > max_monun:
        sticker.pop(i) # 범위 초과
# 모든 경우의 수 탐색-> 둘씩 짝 지을 수 있는 모든 경우의 수(조합)
c = []
for i in range(len(sticker)-1):
    for j in range(i+1,len(sticker)):
        c.append([sticker[i],sticker[j]])

max_size = 0
for i in range(len(c)):
    if c[i][0][0] + c[i][1][0] <= max_monun or c[i][0][0] + c[i][1][1] <= max_monun or c[i][0][1] + c[i][1][0] <= max_monun or c[i][0][1] + c[i][1][1] <= max_monun:
        # 어떻게 더하든 모두 제일 긴 변보다 크다면 -> 의 반대 : 하나라도 작은 값이 있다면
        size = (c[i][0][0] * c[i][0][1]) + (c[i][1][0] * c[i][1][1])
        max_size = max(size, max_size)
print(max_size)


