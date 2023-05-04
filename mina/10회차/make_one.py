N = int(input())
cnt = 0
arr = [0] * (N + 1)
for i in range(N-1 , 0, -1):
    num1, num2, num3 = i + 1, i * 2, i * 3
    if num2 > N:
        arr[i] = arr[num1] + 1
    elif num3 > N:
        arr[i] = min(arr[num1],arr[num2]) + 1
    else:
        arr[i] = min(arr[num1], arr[num2], arr[num3]) + 1

print(arr[1])  