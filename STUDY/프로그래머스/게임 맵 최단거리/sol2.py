maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
now_i = 0 # 현재 x 좌표
now_j = 0 # 현재 y 좌표

n = len(maps) - 1 # 상대 팀 진영의 x 좌표
m = len((maps[0])) - 1 # 상대 팀 진영의 y 좌표
print(len(maps), len((maps[0])) - 1)
answer = 1 # 이동 칸 개수

# for i in range(len(maps)):
#     for j in range(len(maps[0])):
#         if maps[i][j+1] == 1:

while now_i != n or now_j != m: # 상대 팀 진영에 도착할 때까지
    if maps[n][m-1] == 0 and maps[n-1][m] == 0: # 상대 팀 진영이 막혀있으면
        answer = -1
        break
    # if now_i+1 <= n and now_j+1 <= m:
    elif now_j+1 <= m and maps[now_i][now_j+1] == 1: # 오른쪽이 1이라면
        maps[now_i][now_j] = 0 # 현재 지점 0으로 바꾸고
        now_j += 1 # 해당 위치로 이동
        answer += 1
    elif now_i+1 <= n and maps[now_i+1][now_j] == 1 : # 아래가 1이라면
        maps[now_i][now_j] = 0 # 현재 지점 0으로 바꾸고
        now_i += 1 # 해당 위치로 이동
        answer += 1

    elif now_i-1 > 0 and maps[now_i-1][now_j] == 1: # 위가 1이라면
        maps[now_i][now_j] = 0 # 현재 지점 0으로 바꾸고
        now_i -= 1 # 해당 위치로 이동
        answer += 1

    elif now_j-1 > 0 and maps[now_i][now_j - 1] == 1 : # 왼쪽이 1이라면
        maps[now_i][now_j] = 0 # 현재 지점 0으로 바꾸고
        now_j -= 1 # 해당 위치로 이동
        answer += 1

    # else:
    #     answer = -1
    #     break

print(answer)