# 문제
# N(2≤N≤10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.
# 영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다. 물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다. 그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다. 만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.
# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N, M(1≤M≤100,000)이 주어진다. 다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1≤A, B≤N), C(1≤C≤1,000,000,000)가 주어진다. 이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다. 서로 같은 두 도시 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다. 마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다. 공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.
#
# 출력
# 첫째 줄에 답을 출력한다.

input_list = [
    (1, 2, 2),
    (1, 3, 3),
    (1, 4, 5),
    (2, 3, 2),
    (3, 4, 4)
]


# 내가 생각해본 케이스
# 4 5
# 1 2 3
# 1 3 3
# 1 4 5
# 2 3 2
# 3 4 4
# 1 3

def make_graph(input_list):
    graph = dict()

    for t in input_list:
        if t[0] not in graph.keys():
            graph[t[0]] = dict()
        if t[1] not in graph.keys():
            graph[t[1]] = dict()
        graph[t[0]][t[1]] = t[2]
        graph[t[1]][t[0]] = t[2]
    return graph


# graph = make_graph(input_list)


# print(len(graph))
# for i in graph.keys():
#     print(i, graph[i])
# Weight_list = []

# find(graph, 1,       3    , [],          0)
def find(graph, current_node, dest_node, visited_list, current_weight):
    # print("graph:", graph)
    # print("current_node: ",current_node,"current_weight:",current_weight,"visited_list: ",visited_list)
    if current_node == dest_node:
        # print("append into weight_list: ", current_weight)
        Weight_list.append(current_weight)
        return

    visited_list.append(current_node)
    # print("graph[current_node]: ", graph[current_node])
    for next_node in graph[current_node].keys():
        if next_node in visited_list:
            continue
        if current_weight == 0 or current_weight > graph[current_node][next_node]:
            next_weight = graph[current_node][next_node]
        else:
            next_weight = current_weight
        find(graph, next_node, dest_node, visited_list, next_weight)
    visited_list.pop()


# find(graph, 1, 3, [], 0)
# print(Weight_list)


# <<< TEST CODE >>> Start...
N = 4
M = 5
input_list = [
    (1, 2, 2),
    (1, 3, 3),
    (1, 4, 5),
    (2, 3, 2),
    (3, 4, 4)
]

# N = 3
# M = 3
# input_list = [
#     (1, 2, 2),
#     (3, 1, 3),
#     (2, 3, 2)
# ]


start = 1
end = 3

answer = 4

graph = make_graph(input_list)
Weight_list = []
find(graph, start, end, [], 0)
assert max(Weight_list) is answer
# exit()
# <<< TEST CODE >>> End...

# N, M = map(int, input().split(' '))
# input_list = []
# for _ in range(M):
#     A, B, C = map(int, input().split(' '))
#     input_list.append((A, B, C))
# start, end = map(int, input().split(' '))
# Weight_list = []
#
# graph = make_graph(input_list)
# find(graph, start, end, [], 0)
# print(max(Weight_list))

# exit()


# 제출했는데, 틀렸다....폭망...(틀릴걸알고있었다. 하루종일 삽질했는데 맞겠나..실은 이미 직감하고있었다. 난...OTL)
#
# find(graph, 1, 3, visited=[], weight=0, weight_list=[])
# visited += [1]
# if weight > graph[1][2]
#     weight = graph[1][2] // 2
# find(graph, 2, 3, visited=[1], weight=2, weight_list=[])
# visited += [2]
# if weight > graph[2][1]
#     weight = graph[1][2]
#
# find(graph, 1, 3, visited=[1, 2], weight=..., weight_list=[])
# 이전에
# return
# find(graph, 3, 3, visited=[1, 2], weight=2, weight_list=[])
#
#
# def find(graph, start, end):
#     if
#         for node in graph[start].keys():
#             find(graph, graph[node], end)
#
#
# for node in graph.keys():
#     print(graph[node])
# exit()
#
# Weight_list = []
#
#
# def test():
#     print("test")
#     Weight_list.append(1)
#
#
# test()
# print(Weight_list)
# exit()
#
#
# def dfs_recursive(graph, current, dest, weight, visited=[]):
#     if current == dest:
#         if weight > graph[current][dest]:
#             Weight_list.append(graph[current][dest])
#         else:
#             Weight_list.append(weight)
#         return
#     if current in visited:
#         return
#
#     # visited = visited + [start]  ## visited.append(start)대신 visited = visited + [start]를 대입
#     visited.append(current)
#     # print(visited)  # print(visited) 추가
#
#     for node in graph.keys():
#         if node not in visited:
#             weight = graph[node]
#             dfs_recursive(graph[node], node, dest, weight, visited)
#
#     # for node in graph[start]:
#     #     if node not in visited:
#     #         visited = dfs_recursive(graph, node, visited)  # 수정된 부분!
#
#     return visited
#









# 새로운 시작... with 강의해설...OTL

# 핵심아이디어
# -문제이해가 먼저다.
# -다리개수 M: 최대 10만, 중량 C: 최대 10억  //10억나오는 순간 바로 시간복잡도에 루트 혹은 log가 등장하는 알고리즘을 고려. 즉 이진탐색.
# -여기선 아무래도 경로찾는 문제이기때문에, 그래프탐색 알고리즘(BFS,DFS). 우리는 BFS 너비우선방식 사용예정.
# -BFS의 시간복잡도는 O(V+E)이다. 대략 O(M)
# -이진탐색의 시간복잡도는 O(NlogN)이다. 대략 O(logC) //맞나?...쩝...
# -그 결과, BFSX이진탐색 의 시간복잡도 콤보는 O(MlogC) = 10만 * 30 = 300만 (참고로, 파이썬의 연산리미트 2000천만. 최대 5천만까지 봐줌)


# 핵심아이디어1 : 이진탐색
# -보통의 이진탐색의 과정은
#   1 범위의 중간값 뽑기
#   2.1 뽑은 중간값이 찾는 값이면 True리턴
#   2.2 뽑는 중간값이 찾는값이 아니라면 좌우를 선택해서 다시 이진탐색 시작
# -보통의 알고리즘테스트에서의 이진탐색 문제는 조금 다르다. (이 문제와 이전문제인 공유기 설치문제에서 그렇듯.)
#   1 우선 result에 범위의 최소값을 넣기 //최소값은 당연히 문제의 조건을 통과
#   2 범위의 중간값 뽑기 //min~mid~max
#   3.1 뽑는 중간값이 문제의 조건을 통과한다면 result=mid, 큰범위(mid+1 ~ max)에서 다시 이진탐색.
#   3.2 뽑는 중간값이 문제의 조건을 통과하지못하면 작은범위(min ~ mid-1)에서 다시 이진탐색.
#
# -뭐랄까...비슷하면서도 서로 다른듯하다. 그래서 처음에 얏봤다가 큰코다쳤다
# -이진탐색은 2종류의 구현법이있다. (재귀 or 반복문) 아래는 재귀적으로 구현한 이진탐색이다.
# -개인적으로는 반복문을 이용한 구현법이 훨씬더 깔끔한 느낌이긴하다.

def binary_search(data, search):
    print(data)
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    medium = len(data) // 2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium + 1:], search)  # 이런식으로 리스트를 이용해도 재귀함수내에서 문제없나보구나!! 신기!!
        else:
            return binary_search(data[:medium], search)


# 핵심아이디어2 : BFS
# - BFS는 오랜만이다. 알고리즘 공부하면서 이 테스트 강의도 함께 들었어야했나보다. 알고리즘 공부를 선행했다보니 알고리즘 내용들이 가물가물하다
# - 알고리즘 특성상 다시 본다고해도 바로 바로 머리에 들어오지 않아서 문제인데, 그래도 복습해보자. 물론 간단한 코드유형만!
#
# - 무엇보다도 BFS가 뭔지부터 알고가자. BFS를 뭐에 쓰는걸까? 맞다. 너비우선탐색이라는 이름에 걸맞게 탐색용이다.
#   그래프내의 모든 노드를 한번씩 찍는 작업을 얘기하는데, 너비우선식으로 진행한다는 얘기다.
# - 아래는 재귀적으로 구현한 BFS이다. 참고로 BFS는 시간복잡도가 O(V+E)이다. //Vertex,Edge
# - 위에서 설명한 그대로의 코드내용이므로,

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'G', 'H', 'I'],
    'D': ['B', 'E', 'F'],
    'E': ['D'],
    'F': ['D'],
    'G': ['C'],
    'H': ['C'],
    'I': ['C', 'J'],
    'J': ['I']
}


def bfs(graph, start_node):  ### 강사왈...bfs정도는 알고리즘을 그냥 외우는것도 괜찮다고!!~~!
    visited = list()
    need_visit = list()  ## BFS의 구현은 이 2가지 큐가 있는게 포인트!!!

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)  # pop(0)하면 뒤에서 앞으로 채워져서...정말 큐의 pop한 효과!
        if node not in visited:  # not in...참 편하다!! 리스트를 뒤지는 방법!
            visited.append(node)
            need_visit.extend(graph[node])  # 참고 리스트.extend([1,3])은 리스트끼리 합치는 함수다. 굉장히 편하다.

    return visited


bfs(graph, 'A')

# - 딱봐도 사이즈가 나온다. BFS 너비우선탐색의 원리를 구현하기 위해서 need_visit이라는 큐를 사용하고 있다.
# - 이걸 보니, DFS는 구현법이 다르겠다는 생각이 문득 든다.
# - 맞다. 코드가 BFS와 거의 유사하지만, DFS에서는 원리상 need_visit을 스택으로 쓴다는게 포인트다 (생각해보니 왜 스택을 쓰는지 알겠다..)








print("test_input. just copy and paste that...")
s = "4 5\n"+"1 2 3\n"+"1 3 3\n"+"1 4 5\n"+"2 3 2\n"+"3 4 4\n"+"1 3\n"
print(s)


# 핵심원리를 익혔으니, 우선 코드부터 보자. 이거때문에 시간을 너무 잡아먹었으니 조금만 봐주길... -_-

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]


def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = True

    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)

    return visited[end_node]

# 여기서 구현된 BFS는 뭔가 조금 다르다..."코팅테스트"에서 구현해야하는 BFS가 바로 이거다! 랄까?
#
# 쉽게 구현하려면 보통 visited큐를 처음엔 그냥 일반 빈 리스트로 구현하는데,
# 여기서는 노드개수만큼 노드별로 모두 Fasle로 초기화한 리스트로 준비한다.
# 그 이유는 visited[노드]로 방문여부를 체크하는게, 노드 in visited로 체크하는 것보다 빠를 것이기때문인듯 하다...
# 그리고 여기서 굳이 리스트.pop(0)이 아닌 deque.popleft()를 쓴이유는 후자가 성능이 월등하다고.
# 전자가 O(N)인 반면에, 후자는 O(1)이라고.  //헐 pop(0)이 생긴거랑 다르게 O(N)이라니...
# https://docs.python.org/2/library/collections.html#deque-objects

# Q. 처음엔 약간 의뭉스러운 부분도 있었다.. 왜냐하면 BFS코드자체는 주어진그래프와 시작노드를 가지고 나머지 모든노드를 한번씩 방문한다는
# 것을 필수로 하는 알고리즘이다. 즉 BFS()를 실행하면 너비우선방식으로 전부 한번씩 훑는다. 여기서도 이진탐색에서의 '문제의 조건'에 체크를
# BFS()로 한다는말은 매번 훑어야한다는 얘기인데?
# A. 그런데 다시보니 내가 놓치고 있는 부분이 있었다. BFS()가 일반 BFS()가 아니다. 이문제에 특화된 BFS였다. 그냥 성능만 약간 고려한 BFS가
# 아니었다는 얘기다. 위의 방문할 대상을 enQueue하는 부분에서 일반BFS처럼 모조리 다 넣는게 아니라, 주어진 c(하중)값을 감당할 수 있는 다리의 노드들만
# enQueue 하고있다.
# 다시 말해, 일반 bfs()가 그냥 시작노드로부터 모든 노드를 너비우선방식으로 탐색하는 거라면, 여기서 구현한 bfs(c)에서는
# c하중을 가지고 가능한 노드들만 탐색하는 것이다.

# BFS, DFS의 코드상의 핵심 아이디어
# - 다음에도 잊어버릴까봐 한번더 적어보자면, BFS든 DFS든
#  그래프를 구성하고, //여기서의 그래프는 노드별로 붙어있는 엣지들을 중복생각안하고 모두 적어주는 방식. 리스트로든 딕셔너리로든
#  visited리스트와 need_visit리스트를 만든후,
#  시작노드를 need_visit리스트에 넣은후, 팝한여 거기에 연결된 노드들에 대해서 체크해가며 본격 프로세스가 시작된다.
# - 핵심아이디어는 need_visit에 대한부분이다. BFS라면 need_visit을 큐로 만들기때문에 팝하면 FIFO이기때문에 BFS가 된다 .
#  그런데 DFS라면 need_visit을 스택을 만들어서 팝하면 LIFO하기때문에 가장 최근에 넣은게 먼저 팝돼서 방문하게 되니
#  깊이우선방식이 구현되는 것이다.

start = 1000000000
end = 1

for _ in range(m):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)


start_node, end_node = map(int, input().split())
# print(adj)
# print(start,end)
# print(start_node, end_node)

result = start
print(bfs(result))
while (start <= end):
    mid = (start + end) // 2  # mid는 현재의 중량을 의미합니다.
    if bfs(mid):  # 이동이 가능하므로, 중량을 증가시킵니다.
        result = mid
        start = mid + 1
    else:  # 이동이 불가능하므로, 중량을 감소시킵니다.
        end = mid - 1

print(result)


# input
# :
# 3 3
# 1 2 2
# 3 1 3
# 2 3 2
# 1 3

# 입력값에 따라 완성된 adj의 형태
#     : [[], [(2, 2), (3, 3)], [(1, 2), (3, 2)], [(1, 3), (2, 2)]]

# 내가 생각해본 예
# 4 5
# 1 2 3
# 1 3 3
# 1 4 5
# 2 3 2
# 3 4 4
# 1 3

