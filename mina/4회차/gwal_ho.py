func =input()+'+' # '+'는 마지막을 위해 달아줌

val = '' # 두자리, 세자리 수를 묶어주기위해
code ='+' 
stack= [] 

for i in func: # 문자열을 돌아가면서
    if i not in '+-': # 부호가 아니면
        val+=i # val에 넣어준다.
    else: # 부호가 나오면
        if i=='-': # 만약 i가 '-'이면
            code = i # code = i 즉, '-'로 바꿔주고
        stack.append(int(val)) # stack에 모은 숫자를 넣고
        val = code # val에 code를 먼저 넣어줌. ex) '-'가 나오면 -50으로 저장,

print(sum(stack)) # 다  더해줌