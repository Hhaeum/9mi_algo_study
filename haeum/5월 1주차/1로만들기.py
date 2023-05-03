def bfs(N):
    queue = [(N, 0)]

    while queue:
        num, cnt = queue.pop(0)
        memory[num] = cnt
        if num == 1:
            return cnt

        if not num % 2:
            if num // 2 not in memory:
                queue.append((num // 2, cnt + 1))
        if not num % 3:
            if num // 3 not in memory:
                queue.append((num // 3, cnt + 1))
        if num - 1 not in memory:
            queue.append((num - 1, cnt + 1))


N = int(input())
memory = {}
print(bfs(N))