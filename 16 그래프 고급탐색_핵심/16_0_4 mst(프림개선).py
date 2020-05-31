# 개선된프림알고리즘
# 매커니즘은 기존 프림을 얘기하는 경우가 많지만,
# 보통 시간복잡도얘기하면 개선된 프림의 알고리즘을 얘기하는 경우가 있다고.
# (ElogE >> ElogV)

# 기존의 프림은 그래프 = edge리스트 였다. [(x,y,weight), ...]
# 개선된 프림은 그래프 = 노드중심의 dict    //아래 참고


mygraph = {  # 역시 개선된 프림알고리즘이 노드중심이기때문에 노드중심으로 정보를 구성했다....(기존 프림알고리즘이 간선 중심이라서 그래프도 간선중심으로 정보를 구성했지...)
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}

from heapdict import heapdict


def advanced_prim(graph, start):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
    for key in graph.keys():
        keys[key] = float('inf')
        pi[key] = 0
    keys[start] = 0
    pi[start] = start

    while keys:
        current_node, current_weight = keys.popitem()
        mst.append((pi[current_node], current_node, current_weight))
        total_weight += current_weight
        for adj_node, adj_weight in graph[current_node].items():  # 탐험...
            if adj_node in keys and adj_weight < keys[adj_node]:  # 쓸모 체크...

                keys[adj_node] = adj_weight  # 깃발 꽂기...
                pi[adj_node] = current_node

    return mst, total_weight
print(advanced_prim(mygraph,'A'))

exit()

from heapdict import heapdict


def prim(graph, start):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
    for node in graph.keys():
        keys[node] = float('inf')
        pi[node] = None
    keys[start], pi[start] = 0, start

    while keys:
        current_node, current_key = keys.popitem()
        mst.append([pi[current_node], current_node, current_key])  # (출발점,도착점,weight)
        total_weight += current_key  # 개선된 알고리즘에선 total_weight를 따로 계산해주네~ 굳이 ㅋㅋ...(물론 최소신장트리의 1st목표가 최소 가중치다!!)
        for adjacent, weight in mygraph[current_node].items():  # ㅋㅋ 프림알고리즘 아니랄까봐...퍼져나가면서 데이터도 업데이트해가네..
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight  # 노드의 키값을 더 작은 값으로 update!!  # 참고로) keys가 heapdict()구조인 덕에 값이 update되면 내부적으로 자동으로 heapify된다고...캬...
                pi[adjacent] = current_node  # 노드의 키값 update에 대한 hitory....(이 노드의 키값은 저 노드로부터 연결되어 되었다오..)

    return mst, total_weight


# heapdict 사용 tip!
# if adjacent in keys and weight < keys[adjacent]:
# 에서는 첫번째 사실관계에서 탈락하기때문에, 두번째 사실관계 파악을 하지 않는다.


mst, total_weight = prim(mygraph, 'A')
print('MST:', mst)
print('Total Weight:', total_weight)  # 신기하게 기존 프림알고리즘과 결과는 똑같다!!
