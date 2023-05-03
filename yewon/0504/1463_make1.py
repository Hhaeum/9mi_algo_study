from collections import deque
N = int(input())
visited = [0] * 1000000
def bfs(n,cnt):
    queue = deque()
    queue.append((n,cnt))
    while queue:
        cn,ccnt = queue.popleft()
        if cn == 1:
            return ccnt
        if cn % 3 == 0 and 1<= cn // 3 <=1000000 and not visited[cn // 3]:
            queue.append((cn//3,ccnt+1))
        if cn % 2 == 0 and 1<= cn // 2 <=1000000 and not visited[cn // 2]:
            queue.append((cn//2,ccnt+1))
        if 1<= cn - 1 <= 1000000 and not visited[cn-1]:
            queue.append((cn-1,ccnt+1))
print(bfs(N,0))

