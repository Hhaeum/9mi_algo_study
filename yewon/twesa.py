import sys
sys.stdin = open('input.txt')

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]
money_lst = [0]*(N+1)

for i in range(N):
    for j in range(i +lst[i][0],N+1):
        if money_lst[j] < money_lst[i] + lst[i][1]:
            money_lst[j] = money_lst[i] + lst[i][1]

print(money_lst[-1])



