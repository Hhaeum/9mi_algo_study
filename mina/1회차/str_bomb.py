# 문자열이 폭발 문자열을 포함하는 경우, 모든 폭발 문자열이 폭발.
# 남은 문자열을 순서대로 이어 붙여 새로운 문자열 생성
# 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수 있다.
# 폭발 문자열이 없을때까지 계속
# 남아있는 문자가 없으면 FRULA
# 같은 문자 두 개 이상 포함 x

str_v = input()
bomb = input()
length = len(bomb)  # 2
stack = []

i = 0

while i < len(str_v): # str_v의 길이보다 작아야 한다. 0 -> N-1

    stack.append(str_v[i]) # stack에 넣는다.

    # 마지막 글자가 들어올때마다 확인해준다.
    if i >= length - 1 and bomb[-1] == stack[-1]: #마지막 원소와 같은 값이 들어왔을 때 그 전을 확인
        for j in range(1, length + 1):
            if bomb[-j] != stack[-j]: # 혹시 폭탄과 같은가?
                break
        else:
            for _ in range(length): # 길이만큼 stack에서 빼냄
                stack.pop()

    i += 1 # 다음 원소로 이동해서 계속

if not stack: # 스택이 비어잇으면 FRUA를 출력하고
    print('FRULA')
else: # 아니면 그냥 stack 문자열 출력
    print(''.join(stack))

# while로 str_v을 돌면서 stack에 집어넣음
# 만약 문장 안에 bomb 문자열이 있으면 pop()*문자열 만큼
# 완성 되자마자 터짐,