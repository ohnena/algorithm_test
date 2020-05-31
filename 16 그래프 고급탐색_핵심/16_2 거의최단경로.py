# 16.2 거의 최단 경로
# 5719
# medium, 다익스트라 최단경로, 50분


# 이게 최초의 아이디어인데...아이디어는 맞았다! 구현에서 애를 먹었을뿐...OTL....
# 1. 다익스트라 사용하여 distances테이블 구하기
# 2. distances테이블을 이용하여 역추적하여, 최단거리를 만드는 경로의 edge를 모두 구하기 (BFS이용하여 엣지리스트 리턴)
# 3. 구한 edge리스트를 이용하여 기존의 그래프에서 해당 edge정보를 모두 del
# 4. 축소된 그래프에 다시한번 다익스트라 사용하여 최단경로 구하기. 끝



# 합격후 다시 적어보는 소회
# :
# 먼저 이 문제를 풀며 낸 첫 아이디어는 좋았다. 우선 그래프에 다익스트라를 돌려서 distances[]를 완성하고,
# 그걸 이용해서 최단거리 만드는 경로를 그래프에서 삭제한후 다시 다익스트라를 돌린다는 아이디어였다
# 다만 역추적을 BFS를 통해 한다는 정도만 생각했지, 구체적으로 어떻게 할지에 관해서 갈피를 못잡았다.
# (해답에선 dropped를 이용했다. 이렇게 하니 다익스트라 알고리즘 코드수정도 간편하더라.)
#
# 또한 BFS의 기본폼(visited를 사용해야한다는)에만 집착해서인지 BFS구현에 애를 먹었다.
# 해답에선 굉장히 유연하게 코딩했더라. 루프 초기에 popped == start인지를 체크해서 continue하도록 한부분도 그렇고,
# 기존에 visited[x] = True를 하는 부분을 dropped[prev][now] = True로 바꾼 부분도 그렇다.
#
# 아직 수련이 더 필요하다. 이 다음문제는 mst문제이니 복습하고가자. 고생해라...



# 해답기반 새로 >> 합격...
import sys
import heapq
from _collections import deque

while (True):
    nv, ne = map(int, sys.stdin.readline().split())
    if nv == 0 and ne == 0:
        break

    distances = [1e9] * (nv)
    adj = [[] for i in range(nv)]
    reverse_adj = [[] for i in range(nv)]
    dropped = [[False] * (nv) for i in range(nv)]

    start, end = map(int, sys.stdin.readline().split())
    for _ in range(ne):
        x, y, cost = map(int, sys.stdin.readline().split())
        adj[x].append((y, cost))
        reverse_adj[y].append((x, cost))


    def dijkstra():
        heap_data = []
        heapq.heappush(heap_data, (0, start))
        distances[start] = 0

        while heap_data:
            dist, now = heapq.heappop(heap_data)
            if distances[now] < dist:
                continue
            for i in adj[now]:
                cost = dist + i[1]
                if distances[i[0]] > cost and dropped[now][i[0]] != True:
                    distances[i[0]] = cost
                    heapq.heappush(heap_data, (cost, i[0]))


    def bfs():
        need_visit = deque([end])
        while need_visit:
            now = need_visit.popleft()
            if now == start:  # 탐색과정에서 start도착하면 거기서부턴 다시 시작하면 안되지!
                continue
            for prev, cost in reverse_adj[now]:
                if distances[now] == distances[prev] + cost:
                    dropped[prev][now] = True
                    need_visit.append(prev)


    dijkstra()
    # print(distances)
    bfs()
    # for i in range(nv):
    #     for j in range(nv):
    #         if dropped[i][j] == True:
    #             print(i,j)
    # exit()
    distances = [1e9] * (nv)
    dijkstra()



    if distances[end] == 1e9:
        print(-1)
    else:
        print(distances[end])


exit()










# 첫코드 >> 광탈...
nv, ne = map(int, input().split())
start, end = map(int, input().split())

adj = [[] for i in range(nv + 1)]
adj_rev = [[] for i in range(nv + 1)]  # bfs용...
distances = [float('inf')] * (nv + 1)

for _ in range(ne):
    u, v, p = map(int, input().split())
    adj[u].append((v, p))
    adj_rev[v].append((u, p))

import heapq


def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distances[start] = 0

    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distances[now] < dist:
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if distances[i[0]] > cost:
                distances[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))


from collections import deque


def bfs(start):
    result = []

    need_visit = deque([start])
    visited = [False] * (nv + 1)

    while need_visit:
        popped = need_visit.popleft()
        visited[popped] = True  # 다익스트라의 그래프 특성상...최단경로가 여러개 나올 수 있고, 그중에 겹치는 노드가 있지 않을까?
        for adj_node, cost in adj_rev[popped]:
            if visited[adj_node] == False:
                if distances[adj_node] + cost == distances[popped]:
                    result.append((adj_node, popped))
                need_visit.append(adj_node)

    return result


print("간선삭제전", adj)
# 1회차 다익스트라...
dijkstra(start)
print("1회차다익스트라", distances, distances[end])

# 간선삭제
paths = bfs(end)
print(paths)
for x, y in paths:
    for i in range(len(adj[x])):
        if adj[x][i][0] == y:
            del adj[x][i]
            break
            # print("after adj",adj)

print("간선삭제후", adj)

# 2회차 다익스트라...
distances = [float('inf')] * (nv + 1)
dijkstra(start)
print("distances", distances)
if distances[end] == float('inf'):
    print(-1)
else:
    print(distances[end])
