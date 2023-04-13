from collections import deque

N, K = map(int, input().split())

q = deque([(N, 0)])
visit = set()
visit.add(N)

#swea랑 똑같은데..

find = 1
if N == K:
    print(0)
else:        
    while find:
        N, cnt = q.popleft()
        for i in [N * 2, N + 1, N - 1]:
            if i == K:
                print(cnt+1)
                find = 0
                break
            if 0<=i<=100000 and i not in visit:
                q.append((i, cnt + 1))
                visit.add((i))
