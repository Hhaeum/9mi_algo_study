N = int(input())
ans = N-1
i = 1

while True:
    ans -= i*6
    if ans <= 0:
        ans = i
        break
    i += 1

if N == 1:
    ans = 0
print(ans + 1)