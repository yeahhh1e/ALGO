def f(i, k, s, t):  # i: 원소, k: 집합의 크기, s: i-1까지 고려된 합, t: 목표
    global cnt
    if s > t: # 고려한 원소의 합이 찾는 합보다 큰 경우
        return # 남은 원소 고려할 필요 X
    elif s == t: # 남은 원소를 고려할 필요 X 
        cnt += 1
        return
    elif i == k: # 모든 원소 고려
        if s == t:
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i + 1, k, s + A[i], t) # A[i] 포함
        bit[i] = 0
        f(i + 1, k, s, t) # A[i] 미포함





A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
#A = [ i for i in range(1, N+1)]   

key = 10 # 찾으려는 합계 값
cnt = 0  # 합이 key와 같은 부분집합의 수
bit = [0]*N
fcnt = 0
f(0, N, 0, key)
print(cnt, fcnt)