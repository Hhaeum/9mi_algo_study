'''
1부터 N까지 중 중복 없이 M개를 고른 수열 출력하기
수열 속 요소는 공백으로 구분한다. <- 수열을 리스트로 저장해서 언패킹
중복되는 수열을 여러 번 출력하면 안된다. <- 수열 저장 전에 검사하기. set보단 빠를 것 같음.
1, 3과 3,1은 다른 수열이다.
'''


def perm(tmp, cnt):
    # cnt : 수열의 길이, tmp : 저장되지 않은 수열 length <= M
    if cnt == M:  # N개 고르기
        print(*tmp)
        return

    for i in range(N):
        if not used[i]:    # 수열의 요소 중복 사용을 막기 위한 리스트
            used[i] = 1
            tmp.append(arr[i])
            perm(tmp, cnt + 1)
            tmp.pop()   # 사용한 요소는 빼준다.
            used[i] = 0    # 이 요소는 사용하지 않았다고 세팅


N, M = map(int, input().split())
arr = list(range(1, N + 1))
used = [0] * N
perm([], 0)