# 수많은 시간 초과와의 싸움

N = int(input())
arr = list(map(int,input().split()))
new_arr = sorted(list(set(arr))) # 정렬
arr_dict = dict()
# 딕셔너리에 인덱스 넣어주기 999:0 1000:1 처럼
for i in range(len(new_arr)):
    arr_dict[new_arr[i]] = i
for i in range(N):
    print(arr_dict[arr[i]], end=' ')

