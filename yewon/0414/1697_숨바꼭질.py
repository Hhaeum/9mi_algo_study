# 수빈이 x-1로 이동 / x+1 / 2*X

# sw에서 푼 문제랑 좀 비슷하다.
# 트리를 쫙 가로로 다 돌아보고(bfs) K가 나오면 바로 cnt 출력

def bfs(n,m):
    global cnt
    queue = []
    queue.append((n,cnt))
    visited[n] = 1
    while queue:
        cn,ncnt = queue.pop(0)
        if cn == m:
            return ncnt
        #갈림길을 만들어주어요
        if 0<=cn-1<=100000 and not visited[cn-1]:
            queue.append((cn-1,ncnt+1))
            visited[cn-1] = 1

        if 0<=cn+1<=100000 and not visited[cn+1]:
            queue.append((cn+1,ncnt+1))
            visited[cn+1] = 1

        if 0<=(2*cn)<=100000 and not visited[2*cn]:
            queue.append((2*cn,ncnt+1))
            visited[2*cn] = 1


N,K = map(int,input().split())
visited = [0]*100001
cnt = 0
print(bfs(N,K))