
# 1 입력받기
N, M = map(int, input().split())
nodes = []
for _ in range(N):
    x, y = map(int, input().split())
    nodes.append((x,y))
connected_edges = []
for _ in range(M):
    x, y = map(int, input().split())
    connected_edges.append((x,y))

# 2 그래프(edge리스트) 생성


import math
def get_distance(node1,node2):
    a = node1[0] - node2[0]
    b = node1[1] - node2[1]
    return math.sqrt((a*a + b*b))

edges = []
for i in range(N-1):
    for j in range(i+1,N): # 무방향 그래프라서 엣지들의 중복없도록...
        if i == j:
            continue
        # if (i,j) in connected_edges or (j,i) in connected_edges: #이미 연결된 녀석들 제외...
        #     continue
        # dist = math.sqrt((nodes[i][0]-nodes[j][0])**2 + (nodes[i][1]-nodes[j][1])**2)
        dist = get_distance(nodes[i],nodes[j])
        edges.append((dist,i+1,j+1))



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
    # mst = []
    total_cost = 0
    for node in range(N):
        make_set(node)

    for node1, node2 in connected_edges: # 이미 연결된 녀석들 처리...
        union(node1,node2)

    edges.sort()
    for edge in edges:
        cost, node1, node2 = edge
        if find(node1) != find(node2):
            union(node1,node2)
            total_cost += cost
            # mst.append(edge)
    return total_cost

result_cost = kruskal()

print("%.2f" % result_cost)




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
