#
#
# # 기본적인 mst내용은 mst(크루스칼) 파일을 참고...
#
# # 크루스칼과 프림의 차이점은?
# 전자는 간선을 가지고 진행시키고,
# 후자는 노드를 가지고 진행시킨다.
#
# # 첫인상은 프림이 훨씬 더 직관적이다...그래프 순회(DFS,BFS)의 형태도 보이고 말이다...
#
# # 프림의 매커니즘 >> 이거도 다익스트라와 마찬가지로 BFS의 향기가 짙게 난다...
# 1. 시작노드 선택하여, '연결된노드집합'에 삽입
# 2. push한 노드에 대한 연결된 간선들을 '간선리스트'에 삽입
# 3. '간선리스트'에서 weight가 가장 작은 간선을 추출하여 # 그리디...
#     거기에 붙은 인접노드가 '연결된노드집합'에 없다면, '연결된노드집합'에 삽입하고, 거기에 붙은 간선들 '간선리스트'에 삽입
#     있다면, '간선리스트'로부터 해당간선 삭제
# 4. '간선리스트'가 빌때까지 2.3.반복
#
#
# # 구현시 준비사항...
# 아래의 두가지 라이브러리를 사용...
# import heapq,
# from collections import defaultdict # 없는 키에 접근시 KeyError나는 불상사를 없앤다. (없는키는 자동으로 초기화해버림.)
#
#


myedges = [  # 방향으로인한 중복은 모두 제외된 간선 리스트다 !
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

# import * from collections
# import * from heapq

from collections import defaultdict
import heapq


def prim(start_node, edges_list):
    mst = []
    # 필요한 3가지 준비사항...
    # 1 Adjacent Edges (defaultdict)
    adjacent_edges = defaultdict(list)
    for edge in edges_list:
        adjacent_edges[edge[1]].append(edge)
        adjacent_edges[edge[2]].append((edge[0], edge[2], edge[1]))
    # 2 Connected Nodes (set)
    connected_nodes = set(start_node)
    # 3 Candidate Edge List (heapq)
    candidate_edge_list = adjacent_edges[start_node]
    heapq.heapify(candidate_edge_list)

    while candidate_edge_list:
        cand_edge = heapq.heappop(candidate_edge_list)
        if cand_edge[2] in connected_nodes:
            continue

        connected_nodes.add(cand_edge[2])  # 근데, mst리스트를 안쓰고, connected_nodes집합을 굳이 만들어서 쓸까?
        mst.append(cand_edge)  # 굳이 이유를 찾는다면, mst리스트는 는 연결되는 순서도 알 수 있긴해...
        for edge in adjacent_edges[cand_edge[2]]:
            heapq.heappush(candidate_edge_list, edge)

    return mst


print(prim('A', myedges))

# 예상 결과
# [(5, 'A', 'D'),
#  (6, 'D', 'F'),
#  (7, 'A', 'B'),
#  (7, 'B', 'E'),
#  (5, 'E', 'C'),
#  (9, 'E', 'G')]



