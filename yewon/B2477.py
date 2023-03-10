import sys
sys.stdin = open('input.txt')

# 동 서 남 북 1 2 3 4
# 참외밭 넓이 구하기


N = int(input()) # 1당 참외 갯수
# 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돈다;
# 방향, 길이
dir_lst = []
max_w = 0
max_h = 0
max_w_idx = 0
max_h_idx = 0
for i in range(6): # 6각형
    dir, dis = map(int,input().split())
    # 큰 박스 넓이 - 작은 박스 넓이
    dir_lst.append((dir,dis))
    if dir_lst[i][0]== 1 or dir_lst[i][0]== 2:
        if max_h < dir_lst[i][1]:
            max_h = dir_lst[i][1]
            max_h_idx = i
    elif dir_lst[i][0]== 3 or dir_lst[i][0]== 4:
        if max_w < dir_lst[i][1]:
            max_w = dir_lst[i][1]
            max_w_idx = i
big_box = max_w * max_h
small_h = abs(dir_lst[(max_h_idx+1)%6][1] - dir_lst[(max_h_idx-1)%6][1])
small_w = abs(dir_lst[(max_w_idx+1)%6][1] - dir_lst[(max_w_idx-1)%6][1])

# 큰 상자-작은상자 * 1단위당 N
result = (big_box-(small_h * small_w)) * N
print(result)