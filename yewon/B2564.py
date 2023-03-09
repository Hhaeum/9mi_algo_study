import sys
sys.stdin = open('input.txt')


# 마지막은 동근이 위치
# 최단거리 합.

# 어캐푸는지 모르겠어서 아이디어 참고함 (시험치고 다시 풀 것.)
# 아이디어 : 절대 거리를 구해서 case1. abs(동근-상점)
# case2. 전체 너비 - case1을 해서 더 큰 값을 계속 누적시켜 줍니다. 왔더 !!! 매우 놀라워라

def solve(dir,dist): # 0,0에서 부터의 절대 거리 재는 함수
    if dir == 1: #북쪽
        return dist
    elif dir == 2: #남쪽
        return block_w + block_h + (block_w - dist)
    elif dir == 3: #서쪽
        return block_w + block_w + block_h + block_h - dist
    elif dir == 4: #동쪽
        return block_w + dist

block_w , block_h = map(int,input().strip().split())
N = int(input()) # 상점 개수

dis_lst = []
for _ in range(N+1): #N은 상점개수, 동근이까지 포함해야 함.
    dir, dist = map(int, input().strip().split())
    #동근이 하고 상점 거리를 비교해야 함.
    dis_lst.append(solve(dir,dist))

ans = 0 #결과 출력. 누적합
for i in range(N):
    case1 = abs(dis_lst[-1] - dis_lst[i])
    case2 = 2 * (block_w + block_h) - case1
    ans += min(case1,case2)

print(ans)







