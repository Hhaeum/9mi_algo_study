# def perm(s, cnt):
#     if cnt == 6:
#         print(*lotto)
#         return
#     if N - s < 6 - cnt:
#         return
#     for i in range(s, N):
#         lotto[cnt] = nums[i]
#         perm(i+1, cnt+1)


# while True:
#     try : N, *nums = list(map(int, input().split())) 
#     except : break
#     lotto = [0] * 6
#     perm(0, 0)
#     print()


def solve(idx, cnt, arr):
    global result
    if cnt == 6 and not arr in result:
        result.append(arr[:])
    # 쭉 돌면서 사용하지 않았으면 일단 넣어보기?
    for i in range(idx, k):
        if not used[i]:
            used[i] = 1
            arr.append(S[i])
            solve(i + 1, cnt + 1, arr)
            arr.pop()
            used[i] = 0
            solve(i + 1, cnt, arr)

k = 0
while True:
    try:
        k, *S = map(int, input().split())
        used = [0] * k
        result = []
        solve(0, 0, [])
        for r in result:
            print(*r)
    except:
        break
    print()