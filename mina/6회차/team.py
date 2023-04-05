import sys
sys.stdin = open('sample_input (1).txt', 'r')

T = int(input())

def parent(x):
    if x == people[x]:
        return x
    else:
        return parent(people[x])
    
def union(x,y):
    rx = parent(x)
    ry = parent(y)
    if rx != ry:
        people[rx] = ry

for tc in range(1,T+1):
    N, M = map(int,input().split())
    # N명, M장 신청서
    leader = set()

    paper = list(map(int, input().split()))
    people = list(range(N+1))
    for i in range(0, M*2, 2):
        union(paper[i+1] ,paper[i])
    # print(people)
    for j in range(1,N+1):
        leader.add(parent(j))

    print(f'#{tc} {len(leader)}')
