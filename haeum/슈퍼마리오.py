sum_score = 0
for _ in range(10):
    tmp = int(input())
    if abs(100 - sum_score) >= abs(100 - (sum_score + tmp)):
        sum_score += tmp
    else:
        break
print(sum_score)