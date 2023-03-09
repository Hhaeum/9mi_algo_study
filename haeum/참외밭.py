K = int(input())

tmp = 0
box = []
for _ in range(6):
    _, L = map(int, input().split())
    if tmp:
       box.append(tmp * L)
    else:
        f = L
    tmp = L
box.append(tmp * f)

print((sum(box) - max(box) * 2) * K)
