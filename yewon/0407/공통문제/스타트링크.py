import sys
sys.stdin = open('input.txt')

# 아이디어: N//2로 한 팀을 구성하는 조합을 구한다음,
# 1~N까지의 수에서 한 팀을 뺴면 나머지 한 팀 나옴.
# 그 한 팀에서 또 능력치를 구해주려면 팀 구성원 내의 2명 순열을 만들어줘야 함.
# 순열을 만들어주고 (12,21,13,31...) 그걸 각 팀의 능력치에 더해서
# 절댓값 빼기 해주면 된다.

#조합
def solve(n,r):
    if r == 0:
        result.append(lst[:])
        # 얕은 복사: 주소만 복사함. 슬라이싱을 해줘야 값이 다 들어감.
        return
    if n < r :
        return
    lst[r-1] = n-1
    solve(n-1,r-1)
    solve(n-1,r)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
all_team = [x for x in range(N)]
lst = [0]*(N//2)
result = [] # 조합 담을 리스트
member = [] # 팀을 구분해서 담을 리스트
solve(N,N//2)
# 조합 만들기 완료

for i in result: # result에는 start팀이 담겨있다고 가정
    # link_mem = list(set(all_team) - set(i))
    link_mem = [x for x in all_team if x not in i] # 리스트는 리스트랑 빼기가 안됨
    # set는 되므로 set를 쓰거나
    # 전체 팀멤버에서(0에서 N-1까지) 스타트 팀 빼서 링크 팀 구해줌
    member.append((link_mem,i))

min_v = 0xffffffff
# 참고함 -> 순열 구하기
for mem in member:
    sum_s = 0
    sum_l = 0
    for i in mem[0]: # mem[0]에는 스타트팀 멤버가 담겨있음 ex(0,1,2)
        for j in mem[0]:
            sum_s += arr[i][j]
    for i in mem[1]: # mem[1]에는 링크팀 멤버가 담겨있음 (3,4,5)
        for j in mem[1]:
            sum_l += arr[i][j]
    if min_v > abs(sum_s - sum_l): #능력치 차이 구하기
        min_v = abs(sum_s - sum_l)
print(min_v)