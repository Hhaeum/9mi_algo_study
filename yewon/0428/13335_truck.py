# queue를 이용해서 풀자

truck_cnt, bridge_l, bridge_w = map(int,input().split()) # 트럭 개수, 다리 길이, 다리 하중
trucks = list(map(int,input().split()))
queue = [0]*bridge_l
cnt = 0
i = 0
while queue:
    cnt += 1
    if i < len(trucks):
        queue.pop(0)
        if sum(queue) + trucks[i] <= bridge_w:
            queue.append(trucks[i])
            i += 1
        else:
            queue.append(0) #한칸 전진
    else:
        queue.pop(0)
print(cnt)
