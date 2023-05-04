from collections import deque

start, end = map(int, input().split())

if start == 1:
    start = 2
sosu = [1]*(end+1)
num = int(end**(0.5))

for i in range(2, num+1):
    if sosu[i]:
        for j in range(i*2, end+1, i):
            sosu[j] = 0

for i in range(start, end+1):
    if sosu[i]:
        print(i)
