# 내 위치 - 가려는 방향 차이가 1이면 왼쪽
# 내 위치 - 가려는 방향 차이가 2이면 건너편
# 내 위치 - 가려는 방향 차이가 -1 이면 오른쪽
# 1 : 북     2 : 남       3 : 서       4 : 동

width, height = map(int, input().split())
N = int(input()) # 상점 개수
store = []
answer = 0
# 정보 입력받기
for i in range(N):
    direction, distance = map(int, input().split())
    store.append([direction, distance])

dg_dir, dg_dis = map(int, input().split()) # 동근이 방향, 위치
# 거리 구하기
for i in range(N):
    result = 0
    dir = store[i][0]
    dis = store[i][1]
    if dg_dir == 1: # 북쪽
        if dir == 1: # 북쪽
            result = abs(dg_dis - dis)

        elif dir == 2: # 남쪽
            min_v = dis + height + dg_dis
            if ((width-dg_dis) + height + (width-dis)) < min_v:
                min_v = ((width-dg_dis) + height + (width-dis))
            result = min_v

        elif dir == 3: # 서쪽
            result = dis + dg_dis

        else: # 동쪽
            result = (width-dg_dis) + dis

    elif dg_dir == 2: # 남쪽
        if dir == 1:  # 북쪽
            min_v = dis + height + dg_dis
            if ((width - dg_dis) + height + (width - dis)) < min_v:
                min_v = ((width - dg_dis) + height + (width - dis))
            result = min_v

        elif dir == 2:  # 남쪽
            result = abs(dg_dis - dis)

        elif dir == 3:  # 서쪽
            result = dg_dis + (height-dis)

        else:  # 동쪽
            result = (width - dg_dis) + (height - dis)

    elif dg_dir == 3: # 서쪽
        if dir == 1:  # 북쪽
            result = dg_dis + dis

        elif dir == 2:  # 남쪽
            result = (height-dg_dis) + dis

        elif dir == 3:  # 서쪽
            result = abs(dg_dis - dis)

        else:  # 동쪽
            min_v = dis + width + dg_dis
            if ((height - dg_dis) + width + (height - dis)) < min_v:
                min_v = ((height - dg_dis) + width + (height - dis))
            result = min_v

    else: # 동쪽
        if dir == 1:  # 북쪽
            result = (width - dis) + dg_dis

        elif dir == 2:  # 남쪽
            result = (width - dis) + (height-dg_dis)

        elif dir == 3:  # 서쪽
            min_v = dis + width + dg_dis
            if ((height - dg_dis) + width + (height - dis)) < min_v:
                min_v = ((height - dg_dis) + width + (height - dis))
            result = min_v

        else:  # 동쪽
            result = abs(dg_dis - dis)

    answer += result
print(answer)