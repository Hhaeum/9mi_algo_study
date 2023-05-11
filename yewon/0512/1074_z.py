N, r, c = map(int,input().split())
ans = 0
def Z(n,x,y):
    global ans
    if x==r and y==c:
        print(ans)
        return
    if n == 1: # 가장 나눌 수 없을떄만큼 나누면서 한칸씩 이동
        ans += 1
        return
    if not(x<=r<x+n and y<=c<y+n):
        ans += n*n
        return

    Z(n//2,x,y)
    Z(n//2,x,y+n//2)
    Z(n//2, x+n//2,y)
    Z(n//2,x+n//2,y+n//2)
Z(2**N,0,0)