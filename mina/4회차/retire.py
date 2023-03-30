<<<<<<< HEAD
# # N일 동안 최대한 많은 상담
# 1. 완탐
def consult(start,v): 
    global max_v
    for i in range(start,N): # for문을 돌면서
        if i+T[i] <= N: # 상담 가능한 날짜 안이면
            consult(i+T[i], v+P[i]) # 상담을 함(가능 날짜까지 점프, 돈 구하기)
    else: # 가능한 날짜가 없어서 for문을 벗어나면
        if max_v < v: # 그것이 최대 수익인가?
            max_v = v

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    t,p = map(int, input().split())
    T[i], P[i] = t, p # 각 배열에 넣어줌
max_v = 0 # 최대를 구하는 변수
consult(0,0) # 시작

print(max_v)


# 2. DP

=======
def consult(start,v): # 상담 함수 실행
    global max_v # max_v를 전역 변수 선언
    for i in range(start,N): # 완탐하는데 i가 start,N으로 시작해야함.
        if i+T[i] <= N: # N보다는 작은 수여야함
            consult(i+T[i], v+P[i]) # 재귀
    else: # for문이 다 돌면
        if max_v < v: # max_v를 바꿔준다.
            max_v = v


N = int(input()) 
T = [0]*N
P = [0]*N
for i in range(N):
    t,p = map(int, input().split())
    T[i], P[i] = t, p
max_v = 0
consult(0,0) 

print(max_v)
>>>>>>> f26cc20fd7560fb33dc030e4dc01a531c27583ac
