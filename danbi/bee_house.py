# def house_count(n):
#     if n == 1:
#         return 1
#     else:
#         return house_count(n-1) + 6 * (n-1)

N = int(input())
n = 1
result = 0
while True:
    if n == 1:
        result += 1
    else:
        result += 6 * (n-1)
    if N <= result:
        break
    n += 1

print(n)