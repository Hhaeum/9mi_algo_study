import sys
sys.stdin = open('input.txt')


N = int(input())
time = [list(map(int,input().split())) for _ in range(N)]
# 타임의 1번째가 빠른 아이를 먼저 보고/타임의 0번째가 빠른 아이를 본다
time.sort(key=lambda x: (x[1],x[0]))
#타임을 정렬할건데, x1을 기준으로 보고 정렬후 시작이 빠른거

cnt = 1
end_time = time[0][1]
for i in range(1,N):
    if time[i][0] >= end_time:
        cnt +=1
        end_time = time[i][1]
print(cnt)

