
# 0 1 2 3 4 5 6 7 8 9 있을때
# 0 1 2 3 4 
# 5 6 7 8 9

# 2 3 4 5
# 6 7 8 9 
# 이런식으로 두개씩 줄여나가면서 비교하면 되는데
# 현재 자리수 전까지는 재귀를 돌면서 중복을 모두 체크한 뒤 저장되었기 때문임! 


def check(perm, cnt): # 겹치는지 체크
    s = 0
    n = cnt
    while n > 1: 
        # 같은 수열이 겹치는 경우는 짝수일 때 밖에 없음.
        if n%2: # n이 홀수이면
            s+=1 # 시작값+1
            n-=1 # n-1로 해준다. 
        if perm[cnt-n//2 : ] == perm[s : s+n//2]:
            # 비교했는데 겹치면
            return True # True 반환
        s += 2 # 넘어가면, 다음 으로 넘어간다. 
        n -= 2
    return False


# 작은수 찾기이기 때문에
# 무조건 처음으로 구해지는 수가 작은수다.
# 작은수부터 올려줄거니까! 
# => 즉, 수를 한번 찾고나면 그 다음은 찾을 필요가 없다. 
# if 조건을 걸어서 거르자! 

# 1~3까지의 수 중에 선택하는데, 시간을 줄이기 위해 바로 직전 수만 걸러준다.
# 넣고 쳌
def perm(cnt, pre, total):
    global min_v # 답
    if check(total, cnt): # 만약 중복되는 수열이 있다면
        return # 리턴한 뒤 그 전 자리수를 바꾸어준다.
    if cnt == N:
        min_v = int(total)
        return 
    for i in range(1,4):
        if i!=pre and min_v == 0: # 바로 직전 수와 겹치지 않고, 들어있는 수가 없으면
            perm(cnt+1, i, total+str(i))



N = int(input())
min_v = 0
perm(0,0,'')
print(min_v)

