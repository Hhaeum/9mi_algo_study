big_num = 0
small_num = 0
mushroom = 0

for i in range(10):
    num = int(input())
    mushroom += num
    if mushroom == 100:
        break
    elif mushroom > 100: # 숫자를 더했는데 100이 넘었다.
        big_num = mushroom # 그러면 100보다 큰 합계 중 100에 가장 가까운 값이기 때문에 big_num에 넣는다.
        small_num = mushroom - num # 그리고 숫자를 다시 빼서 100보다 작은 100에 가장 가까운 수를 small_num에 넣는다.
        break
if mushroom == 100: # 합한게 딱 100이면 mushroom을 출력
    print(mushroom)
elif mushroom > 100: # 아니라면 100보다 큰 값과 100보다 작은 값의 100과의 차이를 계산
    a = abs(100 - big_num)
    b = abs(100 - small_num)

    if a > b: # b의 차이가 더 작다면 small_num 출력
        print(small_num)
    elif a < b: # a의 차이가 더 작다면 big_num 출력
        print(big_num)
    else: # a와 b의 차이가 같다면 큰 값인 big_num 출력
        print(big_num)
else: # 숫자 10개를 모두 더했는데 100보다 작으면 그냥 최종적으로 다 합산한 값을 출력.
    print(mushroom)