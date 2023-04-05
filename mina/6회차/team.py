# N명 짝수

# 1)팀나누기

def ability(team): # 팀의 강함 측정 ! 
    total = 0
    for i in range(N//2):
        for j in range(N//2):
            total += synerge[team[i]][team[j]]
    return total



def team(s,cnt): # 팀을 나누는 순열을 만들어 줄거임
    global min_v


    ##### 여기 빼면 그냥 순열
    if cnt == N//2: # 1팀이 다 채워졌다면 ! 
        team1_score = ability(team1) # 1팀 능력치 구하기
        n = 0
        for i in range(N): # 1팀에 들어있는 수를 제외하면 2팀
            if i not in team1:
                team2[n] = i
                n += 1
        
        team2_score = ability(team2) # 2팀 능력치도 구해줌

        min_v = min(min_v,abs(team1_score-team2_score))
        return
    #####
    
    
    if N - s < N//2 - cnt:
        return
    
    for i in range(s,N):
        team1[cnt] = i
        team(i + 1, cnt + 1)


N = int(input())
synerge = [list(map(int, input().split())) for _ in range(N)]
team1 = [0]*(N//2)
team2 = [0]*(N//2)
min_v = 5000000
team(0, 0)

print(min_v)