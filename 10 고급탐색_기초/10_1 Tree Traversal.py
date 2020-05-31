# 10.1 트리순회
# 1991
# easy, 트리, 구현, 20분
# //다양한 분야에서 다양하게 출제..
# //너무 기본중에 기본이라 꼭 기억...
# //테스트장에서 실수하기 쉽다. 트리라는게 자료구조이고, 이걸 직접 구현하다보니 실수하기 쉽다.

# 복습)트리순회 3종
# pre_order전위순회: 루트>왼쪽자식>오른쪽자식
# //재귀적용법 필수
# in_order중위순회: 왼쪽자식>루트>오른쪽자식
# //그림상으로도 x축기준으로 왼쪽부터 출력이 되는게 재밌다... (이 개념도 필히 기억하자. 다른문제에서 등장하기도하는 개념)
# post_order후위순회:왼쪽자식>오른쪽자식>루트

# 핵심아이디어
# -기본적으로 "재귀"사용
# -전위순회: 루트출력>왼쪽자식재귀>오른쪽자식재귀
# -중위순회: 왼쪽자식재귀>루트출력>오른쪽자식재귀
# -후위순회: 왼쪽자식재귀>오른쪽자식재귀>루트출력
# //위와같인 3가지 순회에 대하여 재귀적용법을 사용한다면 생각보다 쉽게 구현되겠구나...

# 구상
# -인풋을 받아서 어떻게 트리구조를 프로그래밍해야할까나... //다양한 구현법이 있는데, Node클래스 + 딕셔너리로 하는게 간단! 데이터구조가 적을땐 이렇게 간단하게 하라고...


class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

    def print(self):
        print("data: ", self.data, ", left: ", self.left_node, ", rigth: ", self.right_node)
        # print("data: ", self.data, end="")
        # print(", left: ", self.left_node, end="")
        # print(", rigth: ", self.right_node)



N = 7
input_list = [
    "A B C",  # A가 트리의 root...
    "B D .",
    "C E F",
    "E . .",
    "F . G",
    "D . .",
    "G . ."
]
tree = {}
for i in input_list:
    root, left_node, right_node = map(str, i.split(" "))
    tree[root] = Node(root, left_node, right_node)



N = int(input())
tree = {}
for _ in range(N):
    root, left_node, right_node = map(str, input().split(' '))
    tree[root] = Node(root, left_node, right_node)

    # tree[root].print()


def pre_order(node):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])


def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])


def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')


pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

# ABDCEFG
# DBAECFG
# DBEGFCA
