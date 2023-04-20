N = int(input())
arr = list(map(int, input().split()))
new_arr = set(arr)
order_arr = list(new_arr)
order_arr.sort()
num_dict = {}

for i in range(len(order_arr)):
    num_dict[order_arr[i]] = i

for i in arr:
    print(num_dict[i], end=" ")