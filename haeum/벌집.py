N = int(input())
cnt = 1
room = 0
for i in range(0, 1000000001, 6):
    if N == 1:
        print(1)
        break
    if N <= cnt:
        print(room)
        break
    cnt += i
    room += 1