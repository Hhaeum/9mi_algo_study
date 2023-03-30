# 내가 있는 곳과 그 사람이 있는 곳을 판별한다.
# 무조건 한 쪽으로 이동. 모든 변 - 이동거리와 비교해서 짧은 거.
# 상점 개수는 모두 100이하의 자연수다.
W, H = map(int, input().split())
N = int(input())
#  1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽에 상점이 있음을 의미한다.
store = [0]*N
plus = [0, -2 * (H + W) , H, 0, -(2 * H + W)]
for i in range(N):
    d, p = map(int, input().split())
    store[i] = abs(p + plus[d])

# 동근이 위치n
n, pos = map(int, input().split())
pos += plus[n]
length = (W + H)*2
sum_d = 0
for pos_s in store:
    sum_d += min (abs(pos_s - pos), length - abs(pos_s - pos))
print(sum_d)