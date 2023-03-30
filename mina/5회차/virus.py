# 웜 바이러스에 걸린 컴퓨터와 연결되 컴퓨터 모두 전이
# 1번 컴퓨터가 바이러스에 걸림.
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴수?

# 컴수 100이하. 1번부터 차례대로 번호 매겨짐

N = int(input())
T = int(input())
network = [[0]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(T):
    a, b = map(int, input().split())
    network[a][b] = 1
    network[b][a] = 1

stack = [1]
visited[1] = 1
while stack:
    now = stack[-1]
    for i in range(1,N+1):
        if network[now][i] == 1 and visited[i] == 0:
            stack.append(i)
            visited[i] = 1
            break
    else:
        stack.pop()

print(sum(visited)-1)