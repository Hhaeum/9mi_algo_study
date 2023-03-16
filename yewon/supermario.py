# 버섯 10개
# 합을 최대한 100

import sys
sys.stdin = open('input.txt')

mush_lst = []
for i in range(10):
    mush = int(input()) #버섯 점수
    mush_lst.append(mush)

sum_lst = []
sum_mush = 0
for i in range(10):
    sum_mush += mush_lst[i]
    sum_lst.append(sum_mush)

result = 0
min_v = 100
for i in range(10):
    if abs(100-sum_lst[i]) <= min_v:
        min_v = abs(100-sum_lst[i])
        result = sum_lst[i]
print(result)








