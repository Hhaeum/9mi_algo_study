from collections import deque

def find_min(M):
    cnt = 0
    used = set()
    while M > 0:
        cnt += 1
        j = 0
        s = 0
        for crain in crains:
            for i in range(s, M):
                if crain >= boxes[i]:
                    boxes.remove(boxes[i])
                    M -= 1                        
                    break
                s +=1
    print(cnt)             




N = int(input())
crains = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

crains.sort(reverse = True)
boxes.sort(reverse = True)

if crains[0] < boxes[0]:
    print(-1)
else:
    find_min(M)