# 10_1의 트리순회 코드를 참고..


# 문제
# 이진트리를 다음의 규칙에 따라 행과 열에 번호가 붙어있는 격자 모양의 틀 속에 그리려고 한다. 이때 다음의 규칙에 따라 그리려고 한다.
#
# 이진트리에서 같은 레벨(level)에 있는 노드는 같은 행에 위치한다.
# 한 열에는 한 노드만 존재한다.
# 임의의 노드의 왼쪽 부트리(left subtree)에 있는 노드들은 해당 노드보다 왼쪽의 열에 위치하고, 오른쪽 부트리(right subtree)에 있는 노드들은 해당 노드보다 오른쪽의 열에 위치한다.
# 노드가 배치된 가장 왼쪽 열과 오른쪽 열 사이엔 아무 노드도 없이 비어있는 열은 없다.
# 이와 같은 규칙에 따라 이진트리를 그릴 때 각 레벨의 너비는 그 레벨에 할당된 노드 중 가장 오른쪽에 위치한 노드의 열 번호에서 가장 왼쪽에 위치한 노드의 열 번호를 뺀 값 더하기 1로 정의한다. 트리의 레벨은 가장 위쪽에 있는 루트 노드가 1이고 아래로 1씩 증가한다.
#
# 아래 그림은 어떤 이진트리를 위의 규칙에 따라 그려 본 것이다. 첫 번째 레벨의 너비는 1, 두 번째 레벨의 너비는 13, 3번째, 4번째 레벨의 너비는 각각 18이고, 5번째 레벨의 너비는 13이며, 그리고 6번째 레벨의 너비는 12이다.
#
#
#
# 우리는 주어진 이진트리를 위의 규칙에 따라 그릴 때에 너비가 가장 넓은 레벨과 그 레벨의 너비를 계산하려고 한다. 위의 그림의 예에서 너비가 가장 넓은 레벨은 3번째와 4번째로 그 너비는 18이다. 너비가 가장 넓은 레벨이 두 개 이상 있을 때는 번호가 작은 레벨을 답으로 한다. 그러므로 이 예에 대한 답은 레벨은 3이고, 너비는 18이다.
#
# 임의의 이진트리가 입력으로 주어질 때 너비가 가장 넓은 레벨과 그 레벨의 너비를 출력하는 프로그램을 작성하시오
#
# 입력
# 첫째 줄에 노드의 개수를 나타내는 정수 N(1 ≤ N ≤ 10,000)이 주어진다. 다음 N개의 줄에는 각 줄마다 노드 번호와 해당 노드의 왼쪽 자식 노드와 오른쪽 자식 노드의 번호가 순서대로 주어진다. 노드들의 번호는 1부터 N까지이며, 자식이 없는 경우에는 자식 노드의 번호에 -1이 주어진다.
#
# 출력
# 첫째 줄에 너비가 가장 넓은 레벨과 그 레벨의 너비를 순서대로 출력한다. 너비가 가장 넓은 레벨이 두 개 이상 있을 때에는 번호가 작은 레벨을 출력한다.
#
# 인풋
# 19
# 1 2 3
# 2 4 5
# 3 6 7
# 4 8 -1
# 5 9 10
# 6 11 12
# 7 13 -1
# 8 -1 -1
# 9 14 15
# 10 -1 -1
# 11 16 -1
# 12 -1 -1
# 13 17 -1
# 14 -1 -1
# 15 18 -1
# 16 -1 -1
# 17 -1 19
# 18 -1 -1
# 19 -1 -1
#
# 아웃풋
# 3 18


N = 19
input_list = ["1 2 3",
              "2 4 5",
              "3 6 7",
              "4 8 -1",
              "5 9 10",
              "6 11 12",
              "7 13 -1",
              "8 -1 -1",
              "9 14 15",
              "10 -1 -1",
              "11 16 -1",
              "12 -1 -1",
              "13 17 -1",
              "14 -1 -1",
              "15 18 -1",
              "16 -1 -1",
              "17 -1 19",
              "18 -1 -1",
              "19 -1 -1"]


# post_order(tree['A'])

# ABDCEFG
# DBAECFG
# DBEGFCA


# 1 노드클래스 정의
# 2 in_order(node, level) 함수 정의 //트리의 depth인 level_depth, 순회하는 노드의 x좌표인 x, 이 둘은 global변수
#   - 중위순회를 하면서도, 해당노드의 level에 대하여 x축값의 최소 최대값을 각각 계산 >> 두 리스트 level_min, level_max
#   - 중위순회를 하면서도, 트리의 레벨 level_depth를 계속 계산.
# 3 필요한 변수 선언 및 초기화 >> N, tree딕셔너리, level_min리스트, level_max리스트, root, x, level_depth
# 4 tree를 N개만큼 빈노드로 세팅, level_min과 level_max도 N개만큼 빈리스트로 세팅,
# 5 인풋받아서 비로소 tree세팅
#   - 트리세팅후, 트리내 노드의 루트정보 세팅
# 6 in_order(tree[root],1) 실행
# 7 level_depth와 level_min리스트, level_max리스트을 이용하여, 최종 result_depth, result_width를 구하여 결과출력.


# 1 노드클래스 정의
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.parent = -1
        self.left_node = left_node
        self.right_node = right_node


# 2 in_order(node, level) 함수 정의 //트리의 depth인 level_depth, 순회하는 노드의 x좌표인 x, 이 둘은 global변수
#   - 중위순회를 하면서도, 해당노드의 level에 대하여 x축값의 최소 최대값을 각각 계산 >> 두 리스트 level_min, level_max
#   - 중위순회를 하면서도, 트리의 레벨 level_depth를 계속 계산.
def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)


# 3 필요한 변수 선언 및 초기화 >> N, tree딕셔너리, level_min리스트, level_max리스트, root, x, level_depth
N = int(input())
# N = 19
tree = {}
level_min = [N]  # 레벨별 x축의 min, max값...
level_max = [0]
root = 1
x = 1
level_depth = 0

# 4 tree를 N개만큼 빈노드로 세팅, level_min과 level_max도 N개만큼 빈리스트로 세팅,
for i in range(0, N + 1):
    # key = str(i)
    tree[i] = Node(i, '-1', -1)  # -1이면 해당 자식노드가 없는 것
    level_min.append(N)
    level_max.append(0)


# exit()
# 5 인풋받아서 비로소 tree세팅
#   - 트리세팅후, 트리내 노드의 부모정보 세팅
#   - 트리의 루트노드도 구해보자. (중위순회의 시작노드로 써야된다)
# exit()
# for i in range(len(input_list)):
for _ in range(N):
    data, left_node, right_node = map(int, input().split(' '))
    # data, left_node, right_node = map(int, input_list[i].split(' '))
    tree[data].data = data
    tree[data].left_node = left_node
    tree[data].right_node = right_node

    if tree[data].right_node != -1:
        tree[right_node].parent = tree[data].data
    if tree[data].left_node != -1:
        tree[left_node].parent = tree[data].data

for i in range(1, N+1):
    print(i,"-",tree[i].parent)
    if tree[i].parent == -1:
        print("root:",i)
        root = i
# 6 in_order(tree[root],1) 실행
# exit()
in_order(tree[root], 1)
# 7 level_depth와 level_min리스트, level_max리스트을 이용하여, 최종 result_depth, result_width를 구하여 결과출력.

result_depth = 0
result_width = 0
for i in range(1, N+1):
    width = level_max[i] - level_min[i] + 1
    if width > result_width:
        result_width = width
        result_depth = i

print(result_depth, result_width)





# 소회
# -이번 문제는 Idea가 80%은 먹고들어가는 문제다
# -무슨 idea? 바로 트리의 중위순회시에 탐색순서가 가장왼쪽의 것부터 출력된다는 사실이다.
#  이걸 count해보면 마치 x좌표가 오름차순하는 것처럼 출력된다. 이 노드들의 x좌표를 알고, 그 노드들의 level을 알면,
#  해당 Level에 대한 width는 쉽게 구할 수 있겠다.
# -맞다. 이 문제가 원하는 답은 같은 level상에서의 최대 width를 구하는 것이다.
#  우선 중위순회가 아무래도 재귀적으로 돌아가는거니까, level계산은 어렵지않겠다
# -그럼 width는 어떻게 구해야할까? 순회중에 해당level에 대한 x좌표를 저장해두면되겠다. 한걸음더 나가서 x값에 대한 Max와 min을 저장해두면,
#  마지막에 max-min 이런식으로 쉽게 구할 수도 있겠다. 어쨌든 level_max[레벨] 처럼 접근하는 level_max,level_min리스트를 만들었다
# -이번건 10_1의 일반 트리순회문제보다는 고차원적인게, Node클래스에 .parent정보가 들어간다. 이는 입력받은 값으로부터 루트노드를 구하기위함이다
#  부모노드가 없다면 (-1값이면 부모든 자식이든 노드가 없는걸로 간주) 그건 루트노드가 된다. 딱 한개 나오겠지
# -10_1에서도 그랬지만, tree구현은 {}딕셔너리기반으로 한다. 키:value는 번호:노드객체의 조합이다.
#  키값을 노드번호로 둬야 해당노드에 대한 접근을 딕셔너리로 쉽게 할 수 있다.

# -강사의 얘기대로, 아이디어측면에서는 어찌보면 간단한데, (중위순회의 성질만 알면 말이다)
#  구현자체가 까다로워서 실수하기 쉬운게 함정이다...