# 해답기반. (그래프 생성시 딕셔너리 아닌 리스트로 구현 + distance도 adj로 이름바꿔서 리스트로 구현.) >> 성공!


import heapq
def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distances[start] = 0

    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distances[now] < dist:
            continue
        for next in adj[now]:
            cost = dist + next[1]
            if distances[next[0]] > cost:
                distances[next[0]] = cost
                heapq.heappush(heap_data, (cost, next[0]))




import sys
test_count = int(sys.stdin.readline())
for _ in range(test_count):
    nv, ne, start = map(int, sys.stdin.readline().split())
    adj = [[] for i in range(nv+1)]
    distances = [float('inf')] * (nv+1)

    for i in range(ne):
        trusted, trust, time = map(int, sys.stdin.readline().split())
        adj[trust].append((trusted,time))

    dijkstra(start)
    count = 0
    max_time = 0
    for i in range(1,nv+1):
        if distances[i] != float('inf'):
            count += 1
            if max_time < distances[i]:
                max_time = distances[i]
    print(count, max_time)


exit()

















# 최초의 구상...런타임에러가 났다. 이유는 모르겠다... 해답을 보니 딕셔너리가 아닌 리스트를 이용하더라.

test_case = int(input())
import heapq


def dijkstra(graph, start):
    # 다익스트라1 : distances딕셔너리 세팅
    distances = {node: float('inf') for node in graph.keys()}
    # 다익스트라2 : 우선순위큐 세팅 (heap를 통한 최소힙 이용...)
    queue = []
    distances[start] = 0
    heapq.heappush(queue, [distances[start], start])

    # 다익스트라3: BFS스러운 로직 시작!
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        # 1차 쓸모체크...
        if distances[
            current_node] < current_distance:  # 크면 쓸모있는거고, 같다면 아직 current_node에서 파생된 녀석들에 업데이를 아직 안했을 수도 있으니 쓸모있다고 봐야지!...
            continue
        distances[current_node] = current_distance  # 맞나? 안해도되나?
        for adj, weight in graph[current_node].items():
            distance = current_distance + weight
            # 2차 쓸모체크...
            if distances[adj] > distance:
                distances[adj] = distance
                heapq.heappush(queue, [distance, adj])
    return distances


for _ in range(test_case):
    nv, ne, start = map(int, input().split())
    # 그래프 생성
    mygraph = {}
    for i in range(ne):
        trusted, trust, time = map(int, input().split())
        if trust not in mygraph.keys():
            mygraph[trust] = {}
        mygraph[trust][trusted] = time
        if trusted not in mygraph.keys():  # 이부분 주의! (방향그래프라서, out degree가 없는 노드가 존재하기때문.)
            mygraph[trusted] = {}

    distances = dijkstra(mygraph, start)

    # 최종계산...
    max_time = 0
    count = 0
    for node, time in distances.items():
        if time != float('inf'):
            count += 1
            max_time = max(max_time, time)  # 마지막 컴퓨터가 걸리는 시간이 가장 max하겠지!?

    print(count, max_time)

# 4
# 3 2 2
# 2 1 5
# 3 2 5
#
# 3 3 1
# 2 1 2
# 3 1 8
# 3 2 4
#
# 4 5 1
# 4 1 1
# 2 4 10
# 3 1 2
# 2 3 2
# 3 2 2
#
# 4 5 1
# 3 2 2
# 2 3 2
# 3 1 2
# 2 4 10
# 4 1 1
