# 키로거는 사용자가 누른 명령을 모두 기록. 
# 화살표나 백 스페이스 입력해도 정확한 비밀번호 가능
# 비밀번호는 ? 강산이가 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표
# 문자열은 1,000,000까지. 
# 백스페이스 : '-' , 화살표 < > 
# 커서 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼
# 나머지 문자는 비밀번호의 일부이다. 
# stack무조건!

T = int(input())
for _ in range(T):
    password = input()
    real_pass = [] # 비밀번호를 차곡차곡 쌓을 빈 리스트
    next_pass = [] # '>'를 만나면 젤 위의 비밀번호를 넣어 줄 빈 리스트
    for p in password:
        if p not in '<>-': # p가 부호가 아니면
            real_pass.append(p) # real_pass에 쌓음
        elif real_pass and p == '<': # '<'이고 real_pass가 존재하면
            next_pass.append(real_pass.pop()) # real_pass의 젤 위의 문자를 next_pass에 넣어 
        elif next_pass and p == '>': # '>' 이고 next_pass가 빈 리스트가 아니면
            real_pass.append(next_pass.pop()) # next)pass의 젤 위 문자를 real_pass에 다시 반환
        else: # -이면
            if real_pass and p == '-': #real_pass 젤 위의 문자열을 없애준다.
                real_pass.pop()
    if next_pass: # 문자열이 끝났을 때
        while next_pass: # next_pass에 있는 문자열을 마저 real_pass로 옮겨준다.
            real_pass.append(next_pass.pop())
    print(''.join(real_pass))
