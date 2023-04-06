while True: # 사전 순 출력
    lst = list(map(int, input().split()))
    k = lst.pop(0)
    c = [0] * 6 # 조합
    # result = [] # 조합 다 담아줄 리스트
    if k == 0: #0이 들어오면 입력 끝이라서 브레이크
        break
    # 로또 번호가 6개 뽑는 것으로 정해져 있기 때문에 무식하게 반복문 6개 돌려봄
    for i in range(k-5):
        for j in range(i+1,k-4):
            for l in range(j+1,k-3):
                for o in range(l+1,k-2):
                    for p in range(o+1,k-1):
                        for q in range(p+1,k):
                            print(lst[i],lst[j],lst[l],lst[o],lst[p],lst[q])
    print(end='\n')