
func =input()+'+'

val = ''
code ='+'
stack= []

for i in func:
    if i not in '+-':
        val+=i
    else:
        if i=='-':
            code = i
        stack.append(int(val))
        val = code

print(sum(stack))