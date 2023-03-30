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