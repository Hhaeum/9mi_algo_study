N, K = map(int, input().split())
visited = [0] * (100001)

queue = []
queue.append((N, 0))
while queue:
    X, cnt = queue.pop(0)
    if X == K:
        break

    for i in [(2 * X), (X + 1), (X - 1)]:
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = 1
            queue.append((i, cnt + 1))

print(cnt)