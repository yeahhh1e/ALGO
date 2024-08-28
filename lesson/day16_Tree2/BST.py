'''
7
3 5 1 2 7 4 -5
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None    # 관리할 데이터는 최상위 root

    def insert(self, key):
        if self.root is None:   # 없다면 그냥 삽입
            self.root = Node(key)
        else:
            self._insert(self.root, key)    # 있다면 자리를 찾아서 삽입

    def _insert(self, node, key):
        if key < node.key:  # 작으면 왼쪽을 고려
            if node.left is None:   # 왼쪽에 삽입 가능할 때
                node.left = Node(key)   # 그냥 삽입
            else:   # 왼쪽에 이미 데이터가 있음
                self._insert(node.left, key)    # 재귀로 한 번 더 탐색
        else:   # 크면 오른쪽 고려
            if node.right is None:  # 오른쪽에 삽입 가능할 때
                node.right = Node(key)  # 그냥 삽입
            else:   # 오른쪽에 이미 데이터가 있음
                self._insert(node.right, key)   # 재귀로 한 번 더 탐색

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):   # node: 현재 바라보고 있는 노드
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key) # node.left: 다음 탐색 노드
        else:
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
