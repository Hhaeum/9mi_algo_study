N = int(input())
A = list(map(int, input().split()))
B, C =map(int, input().split())
total = 0

for i in A:
    i -= B
    total += 1
    if i < 0:
        continue
    if i % C == 0:
        total += (i // C)
    else:
        total += (i // C) + 1

print(total)