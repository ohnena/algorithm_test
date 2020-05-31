#
# # mst구하는 알고리즘 2종
# 크루스칼, 프림
#
# # mst란?
# 최소신장트리. minimum spanning tree. (span이란 퍼져나가고 뻗치는 걸 의미.)
#
# # st의 2가지 조건
# 사이클이 없어야한다 (즉 트리의 조건을 만족해야)
# 모든노드를 포함하고 모두가 연결되어야 한다
#
# # //개인적으로 크루스칼 알고리즘에 대한 어려운 기억이 있어서 걱정이 앞선다 ㅎㅎ (union-find법을 사용했던가?)
#
# # 크루스칼 알고리즘의 기본 매커니즘 3단계
# 1 모든 정점을 독립된 집합으로 만들고, 모든 간선을 비용기준으로 정렬한다
# 2 비용이 작은 간선부터 양끝의 두정점을 비교한다  //그래서 탐욕알고리즘 기반이라고 얘기함...
# 3 두정점의 최상위 정점을 확인하고(find) 서로 다를 경우, 두정점을 연결(union)
#
#
# # union-find 알고리즘이란?
# 기본적으로 disjoint set(서로소 집합)을 표현하는데 트리구조를 사용하는 알고리.
# 간단히 말하자면 노드들중에 연결된 녀석들을 찾는다거나, 노드들을 합칠때 사용
#
# # 여기(크루스칼)에서 union-find 알고리즘을 사용하는 이유
# 결론부터 얘기하자면, 우리가 구한 결과mst가 사이클이 없음을 보장하기 위해서이다.
#
# # union-find알고리즘의 매커니즘
# 크루스칼 알고리즘은 그래프에서 mst를 찾는 알고리즘이다
# mst는 기본적으로 사이클이 존재하지 않으면서 모든 노드가 연결되어있어야 하는 그래프이다. (사이클이 없으니 트리라고 할 수도 있겠다.)
# 크루스칼은 그리디알고리즘을 기반으로해서 cost가 작은 간선들부터 서서히 연결해가면서 mst를 완성하는데,
# 연결할 간선들을 찾으려 순회하면서, 이 간선을 연결했을때 사이클이 만들어지지 않도록 하기위해선 그 양측 노드들의 root를 찾아서(find) 비교하여
# 만약 다를경우에 이 노드들 사이의 간선을 연결(union)한다는 개념을 사용한다. 어찌보면 당연한 것.
# 한마디로 크루스칼은 union-find알고리즘을 사용하는 알고리즘이라고 애초부터 정의해야겠다. (질문부터 잘못되었나? ㅋㅋ)
#
#
# # union-find를 구현하는데, 각각 union by rank와 path compression 기법을 사용하는 이유
# union by rank를 사용하면 union-find를 O(N)에서 O(logN)으로 낮추는데, path compression을 함께쓰면 애초에 O(N)을 O(1)로 만들어버림 ㅋㅋ...
# 참고로 O(N)이라는건, A-B-C-D와 같이 트리가 완전히 편향된 트리인 최악의 경우를 가정했을때 나오는 경우임.
#
# find()만돌려도, 해당서브트리의 root를 찾는 path를 O(1)로 줄여버리고 (겸사겸사 ㅋㅋ)
# union()자체도 뭐 그냥 두 서브트리에서 한쪽의 루트를 다른 한쪽의 루트로 붙여 하나의 트리로 합치고, 그 트리의 루트 랭크를 +1 해주는 작업자체가
# 거의 O(1)수준이다. (그래서 시간복잡도를 보면 이 union-find가 사용되는 부분은 O(1)로 책정된다. 다만 이걸 매간선마다 해야하므로 O(E)가 되지...)
#
# # 크루스칼 알고리즘의 시간복잡도에 대한 허무함
# 결론부터 말하자면, 정작 union-find보다 sort()할때의 시간이 더 든다고 ㅋㅋ. (전자는 O(E) 후자는 O(ElogE))
# 매커니즘이 간선을비용기준오름차순으로 정렬하고나서, 작은거부터하나씩꺼내서 union-find해주는 거다.
# 정렬작업은 파이썬 sort()가 아마도 고급탐색기법으로 구현되어서 O(NloN)이므로 O(ElogE)이다.
# 그런데 union-find자체가 대략 O(1)이고 이작업을 매간선마다 하는 것이므로 대략 O(E)이다.
# 즉 O(ElogE) + O(E)이므로 결론적으로 O(ElogE)
# 이말인즉슨 정렬부분에서의 시간이 관건이라는!
#
#
# # * 오랜만에 훑어봤는데, 사실 초기 러닝커브만 빼면 코드는 나름 심플하네..


graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}







parent = dict()
rank = dict()
def make_set(node):
    parent[node] = node # 부모가 없는 경우에는 자기자신을 부모로...
    rank[node] = 0      # 최초에는 랭크 0

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node]) # 재귀적으로 path-compression을 구현...
    return parent[node]

def union(node1, node2):
    if node1 == 'D' and node2 == 'A':
        print("Debug")
    root1 = find(node1)
    root2 = find(node2)

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    else:
        parent[root2] = root1
        if rank[root1] == rank[root2]:
            rank[root1] += 1


def kruskal(grph):

    mst = []
    for node in grph['vertices']:
        make_set(node)

    edges = grph['edges']
    edges.sort()
    for edge in edges:
        cost, node1, node2 = edge
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(edge)

    return mst



print(kruskal(graph))
# 결과...
# [(5, 'A', 'D'),
#  (5, 'C', 'E'),
#  (6, 'D', 'F'),
#  (7, 'A', 'B'),
#  (7, 'B', 'E'),
 # (9, 'E', 'G')]