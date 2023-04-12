def solve(idx):
    global min_v

    if idx == N:
        tmp = 0
        for i in range(N):
            for j in range(i + 1, N):
                if start[i] and start[j]:
                    # 스타트 팀 두 명 더하기
                    tmp += (S[i][j] + S[j][i])
                elif not start[i] and not start[j]:
                    # 링크 팀 두 명 빼기
                    tmp -= (S[i][j] + S[j][i])
        tmp = abs(tmp)
        if tmp < min_v:
            min_v = tmp
        if not min_v:
            re
        return

    # i 번 선수가 start 팀에 선발 된 경우
    start[idx] = 1
    solve(idx + 1)
    # i 번 선수가 start 팀에 선발되지 않은 경우
    start[idx] = 0
    solve(idx + 1)


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
'''
스타트팀과 링크팀의 능력치를 최소로 하는데
두 팀의 인원수는 한 명 이상이나, 같지 않아도 된다.
1. 스타트팀을 어떻게든 선발한 다음에
2. 남은 인원을 링크팀이라 생각하고 능력차를 계산하고, 최소값을 얻는다.
3. 백트래킹은
'''

min_v = 0xfffff
start = [0] * N
solve(0)
print(min_v)