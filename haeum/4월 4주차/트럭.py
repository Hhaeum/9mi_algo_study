n, w, L = map(int, input().split())
truck = list(map(int, input().split()))
queue = [0 for i in range(w)]
ans = 0
bridge = 0

while truck:
    if bridge - queue[0] + truck[0] <= L:   # 앞 트럭 빼고 뒷 트럭 올릴 수 있다
        bridge += (truck[0] - queue[0])
        queue.pop(0)
        queue.append(truck.pop(0))
    else:   # 못 올라감.
        bridge -= queue.pop(0)
        queue.append(0)
    ans += 1

print(ans + w)