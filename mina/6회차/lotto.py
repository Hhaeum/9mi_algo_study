def perm(s, cnt): # 순열을 사용해서
    if cnt == 6: # 6이 되면 lotto 출력
        print(*lotto)
        return
    if N - s < 6 - cnt: # 만약 뽑아야하는 수가 남은 수보다 많다면
        return # 해당 수열은 멈춘다.
    for i in range(s, N): 
        lotto[cnt] = nums[i] # 로또의 cnt번 자리에 넣었다 뺐다..
        perm(i+1, cnt+1)


while True:
    try : N, *nums = list(map(int, input().split())) 
    except : break
    lotto = [0] * 6
    perm(0, 0)
    print()
