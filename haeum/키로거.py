T = int(input())
for _ in range(T):
    before = input()
    stack_origin = []
    stack_temp = []
    for i in before:
        if i == '<':
            if stack_origin:
                stack_temp.append(stack_origin.pop())
        elif i == '>':
            if stack_temp:
                stack_origin.append(stack_temp.pop())
        elif i == '-':
            if stack_origin:
                stack_origin.pop()
        else:
            stack_origin.append(i)
    while stack_temp:
        stack_origin.append(stack_temp.pop())

    print(''.join(stack_origin))













    # before = input()
    # cursor = 0
    # stack = []
    # for i in before:
    #     if i == '<':
    #         if cursor > 0:
    #             cursor -= 1
    #     elif i == '>':
    #         if stack and cursor < len(stack):
    #             cursor += 1
    #     elif i == '-':
    #         if stack and cursor :
    #             cursor -= 1
    #             stack.pop(cursor)
    #     else:
    #         if cursor < len(stack):
    #             stack.insert(cursor, i)
    #             cursor += 1
    #         else:
    #             stack.append(i)
    #             cursor += 1
    #
    # print(''.join(stack))