# 1 / 2 ~ 7까지 (6개) / (그 밑부터) 8~19 20~37 38~61....
N = int(input())
cnt = 1
sum_v = 1

while N > sum_v:
    sum_v += 6 * cnt
    cnt += 1
print(cnt)






