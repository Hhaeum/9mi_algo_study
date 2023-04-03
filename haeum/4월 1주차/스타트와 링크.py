def solve(idx, cnt):
    global minV
    if cnt == N // 2:    # 종료 조건
        tmp = 0
        for i in range(N):
            for j in range(i + 1, N):
                if start[i] and start[j]:   # 둘 다 스타트팀이라면
                    tmp += (S[i][j] + S[j][i])
                elif not start[i] and not start[j]: # 링크팀이라면
                    tmp -= (S[i][j] + S[j][i])

        tmp = abs(tmp)  # 링크팀 쪽이 더 크다면 차이가 음수가 될 수도 있다.
        if tmp < minV:
            minV = tmp

        return

    for i in range(idx, N):
        if not start[i]:
            start[i] = 1
            # idx~i(현재)까지 돌았을 것이기 때문에 idx + 1이 아닌 i + 1해줌
            # idx + 1만 하면 과하게 돌게 된다.
            solve(i + 1, cnt + 1)
            start[i] = 0


N = int(input())    # 짝수. N/2 명으로 팀을 나누어야 함.
S = [list(map(int, input().split())) for _ in range(N)]
'''
S[i][i]는 항상 0. S[i][j]는  i번 사람과 j 번 사람이 같은 팀이면 더해지는 능력치
팀의 능력치는 모든 쌍의 능력치의 합으로, i와 j가 한 팀이라면 S[i][j]와 S[j][i]가 더해짐
두 팀의 능력치 차이를 최소화 하려고 함.

- 요소가 N//2개 있는 부분집합

'''
minV = 0xfffff
start = [0] * N
solve(0, 0)
print(minV)