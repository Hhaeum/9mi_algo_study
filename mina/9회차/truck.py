# 트럭 n개 지나감 순서 변경 x
# 다리의 길이는 w 단위 길이 이며, 단위 시간에 하나의 단위길이만큼 이동 가능.
# 동시에 올라가있는 트럭은 최대 하중인 L보다 작을 것.
# 큐로 풀 수 있는데 배열? 을 두개 만들어야함.
# 1. 입력된 배열
# 2. 다리 길이만한 배열

# 도착하면 0으로 바꾸고 배열에 있는 숫자와 더해서 몇인지 판별 후 하중 아래면 넣는다.
# 그리고 다음 배열로 고고


from collections import deque


N, W, L = map(int, input().split())
# N : 다리를 건너는 트럭 수
# W : 다리 길이
# L : 최대 하중

trucks = deque(list(map(int, input().split())))
bridge = [0]*W

i = 0
time = 0
while trucks:
    bridge[i] = 0
    if (sum(bridge) + trucks[0]) <= L:
        bridge[i] = trucks.popleft()
    i = (i + 1) % W
    time += 1

print(time + W)

