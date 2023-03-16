cham_num = int(input())
list = [[0] * 5 for _ in range(2)]
order = []
len_list = []
for i in range(6):
    direction, length = map(int, input().split())
    if list[0][direction] == 0:
        list[0][direction] = length
    else:
        list[1][direction] = length
    order.append(direction)
    len_list.append(length)

# 1 : 동쪽  2 : 서쪽  3 : 남쪽  4 : 북쪽
if list[1][2] and list[1][3]: # ㄴ 뒤집은 모양
    idx1 = order.index(4)
    idx2 = order.index(1)
    area = len_list[idx1] * len_list[idx2] - (len_list[(idx1+2)%6] * len_list[(idx1+3)%6])
elif list[1][1] and list[1][3]: # ㄱ 모양
    idx1 = order.index(2)
    idx2 = order.index(4)
    area = len_list[idx1] * len_list[idx2] - (len_list[(idx1+2)%6] * len_list[(idx1+3)%6])
elif list[1][2] and list[1][4]: # ㄴ 모양
    idx1 = order.index(1)
    idx2 = order.index(3)
    area = len_list[idx1] * len_list[idx2] - (len_list[(idx1+2)%6] * len_list[(idx1+3)%6])
elif list[1][1] and list[1][4]: # ㄱ 뒤집은 모양
    idx1 = order.index(3)
    idx2 = order.index(2)
    area = len_list[idx1] * len_list[idx2] - (len_list[(idx1+2)%6] * len_list[(idx1+3)%6])

print(area * cham_num)