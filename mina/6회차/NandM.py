N, M = map(int, input().split())

def perm(cnt):
    if cnt==M:  # M개 선택하면 멈춘다.
        print(*nums)
        return
    for i in range(1,N + 1): # 1~N까지
        if used[i] == 0: # 사용 하지 않았으면
            nums[cnt] = i # 넣고
            used[i] = 1 # 사용했다 하고
            perm(cnt + 1)
            used[i] = 0 # 사용 안함으로 바꾸고

used = [0]*(N+1)
nums = [0]*M

perm(0)

