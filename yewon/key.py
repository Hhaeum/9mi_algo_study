
import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    password = list(input())
    left, right = [], []

    for e in password:
        if e == '<':
            if left:
                right.append(left.pop())
        elif e == '>':
            if right:
                left.append(right.pop())
        elif e == '-':
            if left:
                left.pop()
        else:
            left.append(e)
    # result = ''
    # if left:
    #     for j in left:
    #         result += j
    # if right:
    #     for j in range(len(right),-1,-1):
    #         result += right[j]
    #
    # print(result)

    left.extend(reversed(right))
    print(''.join(left))












