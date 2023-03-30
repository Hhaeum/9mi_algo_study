N = int(input())
schedule = [0]*N
for i in range(N):
    start, end = map(int, input().split())
    schedule[i] = (start, end)

schedule.sort() # 0요소를 기준으로
schedule.sort(key = lambda x : x[1]) # 1요소를 기준으로
cnt = 1
end = schedule[0][1]


for i in schedule:
    if i[0] >= end:
        end = i[1]
        cnt+=1
    
print(cnt)