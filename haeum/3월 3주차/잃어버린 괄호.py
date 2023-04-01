Before = input()
tmp = ''
flag = False    # -가 한 번이라도 나오면 True
ans = 0
for b in Before:
    if not(b in ('+', '-')):
        tmp += b
    elif b == '+' and not flag:
       ans += int(tmp)
       tmp = ''
    elif b == '+' and flag: # 앞에 -가 나왔는데 이번에 +가 나왔음
        ans -= int(tmp)
        tmp = ''
    elif b == '-' and not flag:
        flag = True
        ans += int(tmp)
        tmp = ''
    else:
        ans -= int(tmp)
        tmp = ''

if flag:
    ans -= int(tmp)
else:
    ans += int(tmp)