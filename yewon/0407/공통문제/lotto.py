# 조합 구하기.
# 조합 공식은 nCr = n-1Cr-1 + n-1Cr 이므로 재귀로 구현가능
def solve(n,r):
    if r==0:
        result.append(sorted(p)) # 차례대로 정렬, 깊복
        return
    if n<r:
        return
    p[r-1] = lst[n-1]
    solve(n-1,r-1)
    solve(n-1,r)

while True: # 사전 순 출력
    lst = list(map(int, input().split())) # 전체 리스트 인풋 받고
    k = lst.pop(0)  # 맨 앞 값 뺴주기(리스트 개수)
    p = [0] * 6
    result = []
    if k == 0:
        break
    solve(k,6) #조합-> k개에서 6개 뽑는 개수
    result.sort() # 정렬해서 출력
    for row in result:
        print(*row)
    print(end='\n') # 입력 받고 한 줄 띄워주려고