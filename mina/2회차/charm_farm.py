# 1m^2의 넓이에 자라는 참외 개수 헤아림 참외밭 너비 구하기
# ㄱ자거나 90, 180, 70 회전한 모양의 육각형들
# 동쪽 1 서쪽 2 남쪽 3 북쪽 4

N = int(input()) # 밭에서 자라는 참외의 수 개 / m^2
farm = [(0, 0)] * 6
sum_v = 0
for i in range(6):
    d, m = map(int, input().split())
    farm[i] = (d, m)

for i in range(6):
    if farm[i][0]== farm[i-2][0] and farm[i-1][0] == farm[i-3][0]:
        sum_v += farm[i-3][1]*farm[i-2][1]
        sum_v += farm[i][1]*farm[i-5][1]
        break

print(sum_v * N)



