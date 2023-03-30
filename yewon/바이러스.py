# 트리. 연결을 보자. -> 연결 여부를 보기 위해 인접행렬을 만들자.
import sys
sys.stdin = open('input.txt')

def bfs(i):
    global  cnt
    queue = []
    visited = [0]*(N+1)
    queue.append(i)
    while queue:
        ri = queue.pop(0)
        for j in range(len(arr)):
            if arr[ri][j] and not visited[j]:
                queue.append(j)
                visited[j] = 1
                cnt += 1

N = int(input())
node = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(node):
    i,j = map(int,input().split())
    arr[i][j] = 1
    arr[j][i] = 1
cnt = 0
bfs(1)

print(cnt-1)




