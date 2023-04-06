# 순열을 모두 구하는 프로그램

# 1~N까지 자연수 중에서 중복 없이 M개 고른 수열.

def perm(n,m):
    if n == m:
        print(*p)
        return
    for i in range(N):
        if not used[i]:
            p[n] = lst[i]
            used[i] = 1
            perm(n+1,m)
            used[i] = 0

N,M = map(int,input().split())
lst = [x for x in range(1,N+1)]
p = [0] * M # 순열 담아줄 리스트
used = [0] * N # 방문 체크
perm(0,M)