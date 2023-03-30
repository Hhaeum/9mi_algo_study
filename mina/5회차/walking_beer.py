# 맥주는 20개. 50미터에 한 병씩 마심
# 편의점에서 맥주 충전 가능
# t = 테스트 케이스
# n = 맥주를 파는 편의점의 개수 -> 100개 이하
# 상근이네 집, 편의점, 도착지 좌표  -> -32768 ~ 32768 => 32768더해서 생략

from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int,input().split())) for _ in range(N)]
    festival = list(map(int, input().split()))
    # dfs로 해줄 거임
    visited = [0]*(N+1) # 방문 했는가?
    stack = deque([home]) 

    available = 50*20 # 갈 수 있는 길이
    store += [festival] # store + 목적지

    while stack:
        y, x = stack.pop() # 맨 마지막 위치 빼기
        if visited[-1] == 1: # 만약 목적지에 도착했다면 
            break # 멈춰라
        for i in range(N+1): # store를 돌거임.
            if visited[i] == 0: # 만약 방문한 적 없는 곳이면
                ny, nx = store[i][0], store[i][1] # 그 장소의 y와 x좌표가 무엇인가?
                if abs((y-ny))+abs((x-nx)) <= available: # 내가 있는 위치 - 다음 위치만큼의 거리를 구해서 맥주로 갈 수 있따?
                    stack.append([ny, nx]) # stack에 넣어줌
                    visited[i] = 1 # 방문 전적도 바꿔줌.
        # 만약, 갈 수 있는 곳이 없으면, 그 다음으로 이동할 거임! 

    if visited[-1] == 1: # 목적지에 방문했으면
        print('happy') # happy~
    else: # 아니면
<<<<<<< HEAD
        print('sad') # sad`~
=======
        print('sad') # sad`~
>>>>>>> f26cc20fd7560fb33dc030e4dc01a531c27583ac
