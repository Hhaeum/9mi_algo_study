def check(perm, cnt):
    s = 0
    n = cnt
    while n > 1:
        if n%2:
            s+=1
            n-=1
        if perm[cnt-n//2 : ] == perm[s : s+n//2]:
            return True
        s += 1
        n -= 1
    return False



def perm(cnt, pre, total):
    global min_v
    if check(total, cnt):
        return
    # perms[cnt] = total
    if cnt == N:
        min_v = int(total)
        return 
    for i in range(1,4):
        if i!=pre and min_v == 0:
            perm(cnt+1, i, total+str(i))



N = int(input())
min_v = 0
# perms = ['']*81
perm(0,0,'')
print(min_v)

