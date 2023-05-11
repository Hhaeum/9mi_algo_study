for i in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    '''
    떼어낸 스티커와 변을 접한 스티커는 떼어낼 수 없다.
    arr의 각 값은 해당 칸이 선택되었을 때 자신보다 작은 열의 값들로부터 
    얻을 수 있는 가장 큰 값을 나타낸다.
    '''

    # 1번 열 인덱스 값은 자신의 대각선에 있는 0번 열 인덱스의 값을 얻어야한다.
    if n > 1:   # 1 <= n <= 100000
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]

    for i in range(2, n):
        # i - 1번 열은 행과 관계없이 건너뛰고, i - 2번 열을 선택할 수도 있다.
        arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
        arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])

    print(max(arr[0][n - 1], arr[1][n - 1]))