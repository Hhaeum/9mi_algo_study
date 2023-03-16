N = int(input()) # 테스트케이스  개수
for _ in range(N):
    password = [] # 런타임 에러 났기 때문에 stack으로
    empty_list = [] # 이거도 stack
    words = list(input())
    for word in words:
        if word == '<': # 왼쪽으로 커서 옮기기
            if password:
                empty_list.append(password.pop())
        elif word == '>': # 오른쪽으로 커서 옮기기
            if empty_list:
                password.append(empty_list.pop())
        elif word == '-': # -는 백스페이스니까 지움
            if password:
                password.pop()
        else: # 문자인 경우
            password.append(word)
    # 1. 런타임 에러남
    # password = password + reversed(empty_list)
    # 2.틀림
    # empty_list.reverse()
    # password.extend(empty_list)'
    # 3.
    password.extend(reversed(empty_list))

    print("".join(password))