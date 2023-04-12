# 부분집합

def synerge():
    total1 = total2 = 0
    for i in range(N):
        for j in range(i+1, N):
            if team1[i] and team1[j]:
                total1 += ability[i][j] + ability[j][i]
            elif not team1[i] and not team1[j]:
                total2 += ability[i][j] + ability[j][i]
    return total1, total2

def part(s, n, cnt):
    global ans
    if cnt == n:
        # 시너지 계산하고, 다른팀도 쓰고...
        total1, total2 = synerge()
        ans = min(abs(total1-total2), ans)
        return
    if s == N or n - cnt > N - s:
        return
    team1[s] = 1
    part(s+1, n, cnt+1)
    team1[s] = 0    
    part(s+1, n, cnt)
    


N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]
team1 = [0] * (N)
ans = 0xffffffff
for i in range(1, N//2 + 1):
    part(0, i, 0)

print(ans)