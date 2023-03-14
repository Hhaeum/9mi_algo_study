mushroom = [0] * 10
for i in range(10):
    mushroom[i] = int(input())

max_score = abs(100 - mushroom[0])
idx = 0
for i in range(1, 10):
    mushroom[i] += mushroom[i-1]
    total = abs(100-mushroom[i])
    if total <= max_score:
        idx = i
        max_score = total

print(mushroom[idx])




