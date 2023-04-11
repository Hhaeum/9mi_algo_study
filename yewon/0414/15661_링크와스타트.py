


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)] #능력치
# 1/234 12/34 ... 개수가 1이상인 부분집합을 만들고 거기서 하나 뺴면 남은 한 팀이 나옴.

# 부분집합 만들기 비트연산
start = []
num = [x for x in range(N)]
for i in range(1<<N):
    temp = [] # 임시 리스트
    for j in range(N):
        if i & (1<<j):
            temp.append(num[j])
    start.append(temp)
# 한 팀이 0이되면 안되니까 공집합과 자기자신 제외하기
start.remove([])
start.remove([x for x in range(N)])
# 전체에서 스타트 뺴서 링크팀 만들어주기
link = []
for i in range(len(start)):
    link_mem = set(num)-set(start[i])
    link.append(list(link_mem))

# 팀 구성 끗
# 능력치 더해주기
# 팀 내에서 순열 만들기
start_stat = []
for i in start:
    # 스타트 안의 리스트를 돌면서 길이가 2인 순열 만들기
    start_v = 0
    for j in i:
        for k in i:
            start_v += arr[j][k]
    start_stat.append(start_v)
link_stat = []
for i in link:
    # link[i]에서 길이가 2인 순열 만들기
    link_v = 0
    for j in i:
        for k in i:
            link_v += arr[j][k]
    link_stat.append(link_v)
###########팀 구성에 따른 스탯 저장 완료#######
# 최솟값 구하기
min_v = 0xffffffff
for i in range(len(start_stat)):
    min_v = min(abs(start_stat[i]-link_stat[i]),min_v)
print(min_v)