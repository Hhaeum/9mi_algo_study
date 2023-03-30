
import sys
sys.stdin = open('input.txt')

N = int(input())

lst = []
lst2 = []
cnt_lst = []
for i in range(N):
    kg, cm = map(int,input().split())
    lst.append((kg,cm))
    lst2.append((kg,cm))

for i in range(len(lst)):
    cnt=1
    lst2.pop(i)
    for j,k in lst2:
        if lst[i][0] < j and lst[i][1]< k :
            cnt += 1
    lst2.insert(i,lst[i])
    cnt_lst.append(cnt)

print(*cnt_lst)










