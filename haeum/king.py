king, stone, N = input().split()
al_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
           'F': 6, 'G': 7, 'H': 8}
num_dict = dict((v, k) for k, v in al_dict.items())
king = list(king)
k_r, k_c = al_dict[king[0]], int(king[1])
s_r, s_c = al_dict[stone[0]], int(stone[1])
stone = list(stone)
N = int(N)
arr = [input() for _ in range(N)]
direction = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1),
             'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}
while arr:
    dr, dc = direction[arr.pop(0)]
    k_nr, k_nc = k_r + dr, k_c + dc
    s_nr, s_nc = s_r + dr, s_c + dc
    if 0 < k_nr <= 8 and 0 < k_nc <= 8:  # 범위는 1~8임
        if k_nr == s_r and k_nc == s_c:  # 돌이 방해될 때
            if 0 < s_nr <= 8 and 0 < s_nc <= 8:
                s_r, s_c, k_r, k_c = s_nr, s_nc, k_nr, k_nc  # 이동!
        else:  # 방향 안겹침
            k_r, k_c = k_nr, k_nc

print(num_dict[k_r] + str(k_c))
print(num_dict[s_r] + str(s_c))