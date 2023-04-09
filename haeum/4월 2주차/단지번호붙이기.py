def countTown(queue):
    cnt = 1  # 단지에 포함된 집의 개수
    while queue:
        r, c = queue.pop(0)
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == '1' and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))
                    cnt += 1
    return cnt


N = int(input())
arr = [input() for _ in range(N)]

'''
상하좌우로 인접한 1의 개수를 모두 세어서 집의 수를 저장
    - 배열을 차례로 탐색하다 단지를 발견하면 queue에 넣고 BFS
    - visited 배열에 방문했음을 표시하며 같은 단지를 두 번 세지 않도록 함
위에서 저장한 배열을 sort해서 한 줄에 하나씩 출력하기
'''

visited = [[0] * N for _ in range(N)]

all_town = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:  # 방문하지 않은 단지 발견
            visited[i][j] = 1
            all_town.append(countTown([(i, j)]))

print(len(all_town))
all_town.sort()
for i in range(len(all_town)):
    print(all_town[i])
