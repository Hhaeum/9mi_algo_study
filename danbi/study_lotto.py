# n개 중에 r 개 선택하는 조합 알고리즘 사용
# s 는 숫자 리스트에서 r번째 수 고를때 시작할 위치
def solve(n, r, s):
    if r == 0:
        print(*lotto)
        return
    else:
        for i in range(s, n-r+1):
            lotto[6-r] = nums[i]
            solve(n, r-1, i+1) # 숫자 리스트에서 i번째 인덱스 값을 선택했기 때문에 그 다음 인덱스부터 다음 수 선택

while True:
    num_list = list(map(int, input().split()))
    if num_list[0] == 0:
        break
    N = num_list[0]
    nums = num_list[1:]
    lotto = [0] * 6
    solve(N, 6, 0)
    print()