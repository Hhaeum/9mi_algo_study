N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# https://asxpyn.tistory.com/75
# 이차원 배열 정렬하는 법
arr.sort(key=lambda x: (x[1], x[0]))
# x[1] 기준으로 오름차순, 하지만 같다면 x[0] 기준으로 오름차순
# 끝나는 시간이 순차적이어야 효율적인 값을 낼텐데, 끝나는 시간이 같다면
# 시작 시간이 빠른 것부터 찾기

cnt = end = 0
for s, e in arr:
    if s >= end:    # 시작 시간보다 지금까지 쓴 시간이 늦거나 같다면
        cnt += 1    # 회의 한 번 더 가능
        end = e    # 회의 했으니까 끝나는 시간 맞춰줌
print(cnt)