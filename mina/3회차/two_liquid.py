from sys import stdin

N = int(input())
liquid = list(map(int, stdin.readline().split()))

liquid.sort(key = lambda x: abs(x)) # 절대값 기준으로 정렬
a, b = 0, 1 
min_v = abs(liquid[0] + liquid[1]) # 최솟값에 절대값 젤 작은 수 + 두번째로 작은 수 


'''
절대값 기준으로 정렬하면, 내 근처에 어떤 수가 있는지 나온다.
결국 0에 가까운 수가 나와야 하니까 같은 성질의 용액이면 더 큰수가
나와서 min에서 걸러지고 그게 아니면, 나와 젤 근접한 다른 성질의 용액간
합을 구할 수 있다.
'''
for i in range(N-1): # 돌아가면서
    sum_v = abs(liquid[i] + liquid[i+1]) # 앞 뒤를 구한다
    if sum_v < min_v:
        a, b = i, i+1
        min_v = sum_v
    if min_v == 0:
        break

ans = (liquid[a], liquid[b])
print(*sorted(ans))