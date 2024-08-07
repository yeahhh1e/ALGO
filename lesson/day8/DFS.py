import sys
from pprint import pprint

sys.stdin = open("input.txt", "r")
node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

"""
인접 행렬 (adjacency matrix)
- n x n 크기의 정사각형 행렬
- 노드들 간의 연결 관계를 행렬로 표현한 것
- 무방향 그래프에서는
    - 정점 i와 j 사이에 간선이 있다면 matrix[i][j] = matrix[j][i] = 1 -> 대각선을 기준으로 대칭구조
                              없으면 matrix[i][j] = matrix[j][i] = 0
"""

#       A  B  C  D  E  F  G
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],   # A
    [0, 1, 0, 0, 1, 1, 0, 0],   # B
    [0, 1, 0, 0, 0, 1, 0, 0],   # C
    [0, 0, 1, 0, 0, 0, 1, 0],   # D
    [0, 0, 1, 1, 0, 0, 1, 0],   # E
    [0, 0, 0, 0, 1, 1, 0, 1],   # F
    [0, 0, 0, 0, 0, 0, 1, 0]    # G
]

def DFS(s, V):
    # stack에 시작 정점을 push
    stack = [s]
    # 방문 여부를 체크하는 리스트
    visited = [0] * (V + 1)

    # 스택이 빌 때까지 DFS 진행 (스택에 값이 있는 동안 진행)
    while stack:
        # 현재 조사할 노드
        current = stack.pop()

        # 방문하지 않은 노드라면
        if visited[current] == 0:
            # 방문 표시
            visited[current] = 1
            # 방문한 노드 출력
            print(node[current])

            # 현재 노드에서 갈 수 있는 다음 노드들을 스택에 추가 (방문이랑 스택에 기록은 다름.)
            for next in range(V, 0, -1):    # 왜 역순으로 가냐면 C, B 순으로 담아야 B를 먼저 꺼내기 때문이다. (작은 번호의 노드가 스택의 위쪽으로 위치하게 됨)
            # for next in range(1, V+1):    # 큰 번호 우선 탐색을 한다면 (C부터 탐색)
                # 다음 노드가 간선이 연결이 되어 있고 + 방문한 적이 없다면
                if matrix[current][next] == 1 and visited[next] == 0:
                    # stack에 push
                    stack.append(next)


# 인접행렬 만들기
# V = 노드의 개수
# E = 간선의 개수
V, E = map(int, input().split())

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 노드별 간선 정보
data = list(map(int, input().split()))

# 간선 정보를 넣기
# 간선의 개수만큼 반복하면서 넣기
for _ in range(E):
    n1 = data[1 * 2]
    n2 = data[1 * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1
                                                                                                                        
pprint(adj_matrix)




DFS(1, 7)