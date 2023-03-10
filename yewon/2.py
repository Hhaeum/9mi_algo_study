import sys
sys.stdin = open('input.txt')


N = int(input())
# 승환이가 간식을 받을 수 있음!: 스택에 5가 없어야 함.
lst = list(map(int,input().split()))
stack = []
# 만약 수가 지금 들어가야 하는 수가 아닐 때까지 스택에 넣음.
# 들어가야 하는 수가 나오면 스택에 넣지 않고 다음 수로 넘어간다.
num = 1 # 순서
while lst:
    if num == lst[0]:
        lst.pop(0)
        num +=1
    else:
        stack.append(lst.pop(0))
    while stack:
        if stack[-1] == num:
            stack.pop()
            num += 1
        else:
            break


if stack:
    print('Sad')
else:
    print('Nice')






