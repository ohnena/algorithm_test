

# 해답...굉장히 빠르다...심지어 path-compression을 사용하면 더 빨라진다.
import math
import sys
input = sys.stdin.readline

def get_distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    return math.sqrt((a * a) + (b * b))

def get_parent(parent, n):    # path compression X...
    # if parent[n] == n:
    #     return n
    # return get_parent(parent, parent[n])

    if parent[n] != n:
        parent[n] = get_parent(parent, parent[n])
    return parent[n]

def union_parent(parent, a, b): # union-by-rank X...그냥 노드번호로...union-by-number..
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a < b:                   # 그냥 노드 번호가 작은 녀석이 부모가 된다...
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    else:
        return False

edges = []
parent = {}
locations = []
n, m = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x, y))

length = len(locations)
for i in range(length - 1):
    for j in range(i + 1, length):
         edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))

for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

edges.sort(key=lambda data: data[2])

result = 0
for a, b, cost in edges:
    if not find_parent(parent, a, b):
        union_parent(parent, a, b)
        result += cost

print("%0.2f" % result)

# # 3차시도 크루스칼.... >> 탈락....시간초과 OTL.... 당최 어디서 시간초과가 나는 걸까??? >> 헐..PyPy3로 합격!
# >>PyPy3로는 합격했다...헐...그런데 엣지리스트를 만들때, 해당엣지가 connected_edges에 들었는지를 체크하는 부분이 time killer네...
#
# 노드들이 연결된 상태로 주어져버리니, 크루스칼이 아니고서는 불가능하다.
# 왜냐하면 크루스칼은 union-by-rank기법을 사용하여, 사이클 체크가 가능하기때문.
# (개인적으로, 지금까진 프림이든 개선된 프림이든 사이클을 막을 방법을 못찾고있다 ㅠㅠ...없을지도 모름. 길이 있대도...쉬운길두고 굳이...)
#
# # 크루스칼 3형제를 소환해보자
# make_set(node) : node의 rank[node]와 parent[node] 초기화
# find(node) : 재귀적으로 path compression을 구현하고 root를 리턴해줌...
# union(node1,node2) : union-by-rank기법을 이용하여 node1과 node2를 연결(그 둘의 서브트리를 연결함)
#
# # 크루스칼 매커니즘
# 1 edges를 오름차순으로 sorting. edge는 (dist,node1,node2)의 구조.
# 2 edges를 for문 순회하면서, 해당엣지를 mst의 엣지로 사용할지 (즉 두 노드를 연결할지)를 결정
# ex)
# edges.sort()
# for edge in edges:
#     cost, node1, node2 = edge
#     if find(node1) != find(node2):
#         union(node1,node2)
#         total_cost += cost
#         mst.append(edge)

# 1 입력받기
N, M = map(int, input().split())
nodes = [(float('inf'),float('inf'))]
for _ in range(N):
    x, y = map(int, input().split())
    nodes.append((x,y))
connected_edges = []
for _ in range(M):
    x, y = map(int, input().split())
    connected_edges.append((x,y))

# 2 그래프(edge리스트) 생성
import math
edges = []
for i in range(1,N+1):
    for j in range(i,N+1): # 무방향 그래프라서 엣지들의 중복없도록...
        if i == j:
            continue
        if (i,j) in connected_edges or (j,i) in connected_edges: #이미 연결된 녀석들 제외...
            continue
        dist = math.sqrt((nodes[i][0]-nodes[j][0])**2 + (nodes[i][1]-nodes[j][1])**2)
        edges.append((dist,i,j))
print(nodes)
print(connected_edges)
print(edges)
edges.sort()
print(edges)


# 3 크루스칼 3형제 구현
rank = [0] * (N+1)
parent = [0] * (N+1)
def make_set(node):
    rank[node] = 0
    parent[node] = node
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node]) # path compression...
    return parent[node]

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

# 4 크루스칼 알고리즘 구현
def kruskal():
    mst = []
    total_cost = 0
    for node in range(1, N+1):
        make_set(node)

    for node1, node2 in connected_edges: # 이미 연결된 녀석들 처리...
        union(node1,node2)

    edges.sort()
    for edge in edges:
        cost, node1, node2 = edge
        if find(node1) != find(node2):
            union(node1,node2)
            total_cost += cost
            mst.append(edge)
    return total_cost, mst

result_cost, result_mst = kruskal()

print("%.2f" % result_cost)
print(result_mst)
exit()






# 2차시도 개선된 프림 >> 실패



# 개선된 프림으로 도전! >> 실패...아무리 연결된 엣지를 그래프에서 삭제하더라도, 문제가 해결되지 않는다.
# 그이유는, 결과로 받은 mst에 시작전 삭제한 edge들을 넣어보면, 분명 사이클이 나올 테니...
# 결국 답은 크루스칼인듯...연결된 녀석이 존재할땐 크루스칼이 답인듯하다!!! ㅠㅠ
import math
N, M = map(int, input().split())
nodes = [(0,0)]
for _ in range(N):
    x, y = map(int, input().split())
    nodes.append((x,y))
connected_edges = []
connected_nodes = []
for _ in range(M):
    x, y = map(int, input().split())
    connected_edges.append((x,y))
    connected_nodes.append(x)
    connected_nodes.append(y)

# edges
edges = [[] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(i, N+1):
        if i == j:
            continue
        if (i,j) in connected_edges or (j,i) in connected_edges: #이미 연결된 녀석들 제외...
            continue
        dist = math.sqrt((nodes[i][0]-nodes[j][0])**2 + (nodes[i][1]-nodes[j][1])**2)
        edges[i].append((j, dist))
        edges[j].append((i, dist))



from heapdict import heapdict
def advanced_prim():
    mst = []
    total_cost = 0
    keys = heapdict()
    pi = dict()
    for i in range(1,N+1):
        keys[i] = float('inf')
        pi[i] = None


    if i in connected_nodes:
        keys[i] = 0
        pi[i] = i
    while keys:
        cur_node, cur_key = keys.popitem()
        total_cost = cur_key
        mst.append((pi[cur_node],cur_node,cur_key))
        for adj_node, adj_weight in edges[cur_node]:
            if adj_node in keys and adj_weight < keys[adj_node]:
                keys[adj_node] = adj_weight
                pi[adj_node] = cur_node

    return mst, total_cost

mst, total_cost = advanced_prim()
print(nodes)
print(connected_edges)
print(edges)
print("mst", mst)
print(total_cost)

exit()







# 1차 시도 일반프림...실패

# 프림으로 실패후 회고
# :
# 프림을 이용해서 풀었는데, 이문제에는 적합하지 않은 듯하다.
# 프림은 보통 시작점이 주어지고, 거기서부터 퍼져나가면서 connected_nodes에 없는 녀석들을 연결시키는데,
# 여기선 이미 문제시작도 전부터 connected_nodes에 모든 노드가 들어차있다.
#
# 해답에선 크루스칼로 풀었더라.
# 프림으로 구하는 방법은 없을까? 하아....딱히 묘안이 떠오르진 않는다.
#
# 그럼 크루스칼은 여기서 프림이 해결하지 못한 이미 연결된 녀석들에 대한 처리도 가능할까?
# Yes. 크루스칼의 매커니즘자체가 그렇다. 그냥 두노드를 연결시킬까 말까를, 두노드의 root을 비교하여, 같으면 싸이클이 될테니 패스하고,
# 다르면 연결한다. 이런식으로 사이클체크로직이 양측의 root를 비교하는 방식이므로 가능한 것.
# (하지만 프림은 사이클체크방식이 이미 connect한 노드인지 아닌지로 체크한다.)
#
# 잠깐, 개선된 프림을 살펴보니, 왠지 가능할것도 같다.




#
# 4 1
# 1 1
# 3 1
# 2 3
# 4 3
# 1 4
from collections import defaultdict
import math


N, M = map(int, input().split())
nodes = [(0,0)]
for _ in range(N):
    x, y = map(int, input().split())
    nodes.append((x,y))


connected_nodes = []
for _ in range(M):
    x, y = map(int, input().split())
    if x not in connected_nodes:
        connected_nodes.append(x)
    if y not  in connected_nodes:
        connected_nodes.append(y)

adj_edges = defaultdict(list)
for i in range(1,N+1):
    for j in range(i, N+1):
        if i==j:
            continue
        dist = math.sqrt((nodes[i][0]-nodes[j][0])**2 + (nodes[i][1]-nodes[j][1])**2)
        adj_edges[i].append((dist,i,j))
        adj_edges[j].append((dist,j,i))

cand_edge_list = []
import heapq
for x in connected_nodes:
    for edge in adj_edges[x]:
        heapq.heappush(cand_edge_list, edge)

print(nodes)
print(connected_nodes)
print(adj_edges)
print(cand_edge_list)
# 프림 알고리즘 시작...
total_cost = 0
mst = []
while cand_edge_list:
    popped = heapq.heappop(cand_edge_list)
    if popped[2] in connected_nodes:
        continue
    connected_nodes.append(popped[2])
    total_cost = popped[0]
    mst.append(popped)
    for edge in adj_edges[popped[2]]:
        heapq.heappush(cand_edge_list, edge)




print("mst",mst)
print("%.2f" % total_cost)
exit()



# 반례
# :
# 4 2
# 0 0
# 0 1
# 0 2
# 0 3
# 1 4
# 2 3
#
# 결과
# :
# 1 이어야한다.


