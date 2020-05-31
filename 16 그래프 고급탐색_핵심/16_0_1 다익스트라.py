# # 최단경로구하는 유형은 3가지다
# 1 시작점으로부터 특정점까지의 최단경로 구하기 (1:1)
# 2 시작점으로부터 나머지 모든점까지의 최단경로 모두 구하기 (1:N)
# 3 어떤점으로부터 어떤점까지의 최단경로구하기 (N:N...매쉬)
#
# # 다익스트 알고리즘이란?
# -위 유형중 두번째 유형, 시작점이 주어지면 거기로부터 나머지 모든 점까지의 최단경로를 구하는 알고리즘이다.
# -그러므로 기본적으로 distances[모든노드]를 가지고 가야겠구나.
#
# # 다익스트라 알고리즘은 여러가지 구현법이 있다.
# -그중에 우린 최소힙을 이용한다.
# -파이썬에선 heapq라이브버리를 이용하면 된다. ex) heapq.push(리스트, (현재까지 계산된 노드A까지의 최단거리,노드A))
#
# # 참고) 그래프 구현을 위한 dictionary 사용법 숙지
# -for key, value in mygraph.items(): ...
# -for key in mygraph.keys(): ...  //이게 아래와 같다는게 신기!!
# -for key in mygraph
#
#
# # 구현법
#
# 1 그래프 세팅 ex) {노드: {노드:거리, 노드:거리}} ... {'A':{'B':7, 'C':1}, ...}
# 2 다익스트라 함수 구현 dijkstra(graph, start)
#     1) distances딕셔너리 생성 및 inf로 초기화. //다익스트라 알고리즘의 결과값을 계속 업데이트해나갈 딕셔너리! {'A':최단거리, 'B':최단거리, ...}
#     2) 우선순위큐 생성 queue
#     3) start노드에 대한 1),2) 초기화 ex) distances[start] = 0, heapq.heappush(queue, [distances[start], start])
#     4) while queue: // BFS스러운 루프 시작!
#         -우선순위큐에서 heappop: current_distance, current_node
#         -만약 current_distance > distances[current_node]이면, continue  //current_distance, current_node 무쓸모!
#         -쓸모가 있다면, distances[current_node] = current_distance 로 업데이트
#         -for adjacent, weight in graph[current_node]: //업데이트되었으니, 거기서 파생되는 노드들에 대해서도 업데이트할 수 있도록 enqueue!
#             distance = current_distance + weight
#             if distance < distances[adjacent]:
#                 distances[adjacent] = distance
#                 heapq.heappush(queue, [distance, adjacent]) //참고로 거리가 앞에 오게 해야 heapify의 기준이 되어주는거겠지?!
#     5) distances딕셔너리를 return! 끝.
#
# 3 dijkstra(mygraph, start)를 통해 distances를 리턴 받아 처리하고, 프로그램 종료!
#
#
#
#
# # 구현해보자.


mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},        # 이런식으로 방향 그래프다... << 중괄호이용한다는건 파이썬의 딕셔너리 이용한다는 말!
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
} # 테스트용 그래프

# 예상 아웃풋
# {'A': [0, 'A'], 'B': [6, 'C'], 'C': [1, 'A'], 'D': [2, 'A'], 'E': [5, 'D'], 'F': [6, 'E']}

import heapq
def dijkstra(graph, start):
    # 세팅1) distances 딕셔너리 ...
    distances = {node:float('inf') for node in graph.keys() }
    distances[start] = 0

    # 세팅2) 우선순위큐...
    queue = []
    heapq.heappush(queue, [0, start])

    # BFS스럽게 로직시작!
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance: # 쓸모체크... 같은경우는 아직 여기서 파생되는 녀석들을 업데이트 안했다는 표시!
            continue # 이미 쓸고지나갔으니 무쓸모...
        for adj, weight in graph[current_node].items(): # 쓸모있으니, 여기서 파생되는 adj노드들에도 update해주자.
            distance = weight + current_distance
            if distance < distances[adj]: # ajd들에 쓸모체크...
                distances[adj] = distance
                heapq.heappush(queue, [distance, adj])

    # 완성된 distances딕셔너리 리전...끝
    return distances



print(dijkstra(mygraph, 'A'))