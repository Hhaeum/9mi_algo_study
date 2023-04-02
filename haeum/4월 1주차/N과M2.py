def solve(idx, tmp, cnt):
    # 이게 어떻게 백트래킹 문제인가 헀는데
    # 유망한 것만! 검사하는 것도 백트래킹이라 하나봐
    if idx == N: # 유망한지 검사 1
        if cnt == M:# 유망한지 검사 2. 여기서 탈락하는 것도 가지치기겠지...
            print(* tmp)
        return

    tmp.append(arr[idx])
    solve(idx + 1, tmp, cnt + 1)
    tmp.pop()
    solve(idx + 1, tmp, cnt)


N, M = map(int, input().split())
arr = list(range(1, N + 1))
solve(0, [], 0)