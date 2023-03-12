# 키로거는 사용자가 누른 명령을 모두 기록. 
# 화살표나 백 스페이스 입력해도 정확한 비밀번호 가능
# 비밀번호는 ? 강산이가 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표
# 문자열은 1,000,000까지. 
# 백스페이스 : '-' , 화살표 < > 
# 커서 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼
# 나머지 문자는 비밀번호의 일부이다. 
from collections import deque

T = int(input())
for _ in range(T):
    password = input()
    real_pass = deque()
    next_pass = deque()
    for p in password:
        if p not in '<>-':
            real_pass.append(p)
        elif real_pass and p == '<':
            next_pass.append(real_pass.pop())
        elif next_pass and p == '>':
            real_pass.append(next_pass.pop())
        else:
            if real_pass and p == '-':
                real_pass.pop()
        
    print(''.join(real_pass))
