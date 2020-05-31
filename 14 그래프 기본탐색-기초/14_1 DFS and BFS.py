# 유형별문제풀이>14 그래프 기본탐색-기초
# //최근 트렌드문제다..
#
#
# 14.1 DFS와BFS
# 1260
# easy, DFS, BFS, 30분
# //딱 우리가 아는 그거. 기본만 알고 있으면 쉽게 푼다.


# 구상
#
# 1 그래프 구현
# -dict()형식으로 edge정보를 입력
# -ex) graph = {1:[2,3,4], 2:[4], 3:[4]}
# 2 탐색 구현 준비
# -visited, need_visit 두개의 리스트사용
# -BFS일때, need_visit이 큐
# -DFS일때, need_visit이 스택
#
# 3 알고리즘
# 1)need_visit에 start넣기
# 2)need_visit에서 pop하기
#   - if 팝한게 visited에 있드면, pass
#   - else, visited에 넣고 거기에 연결된 v들 모두 need_visit에 넣기
# 3)need_visit빌때까지 2)반복
#
# 4 주의사항
# -위의 조건하에 작은수부터 탐색해야 하므로, 큐와 스택




# 첫 시도....틀렸습니다...탈락 OTL....  >> 수정 보완해서 성공...
# //나름 아이디어를 잘 기억해서 풀었다고 생각했는데 틀렸다
# //물론 중간에 조금 해매긴했다..그래프를 dict와 list조합으로 만들어서..
# //해설을 보니 그냥 그래프를 리스트로만 구현하더라. 애초에 문제에서 노트의 개수 N이 1000이하이고, 노드의 번호는 N이하라고 되어있으니 가능.

nv, ne, start = map(int, input().split())
graph = dict()
for _ in range(ne):
    x, y = map(int, input().split())
    if x not in graph.keys():
        graph[x] = []
        graph[x].append(y)
    else:
        graph[x].append(y)
    if y not in graph.keys():
        graph[y] = []
        graph[y].append(x)
    else:
        graph[y].append(x)

# 스타트 노드가 그래프상에서의 외딴섬일때를 고려.... ( ㅠㅠ 애초에 이런 고민없이 없게하는 코드를 짜야한다... 그래서 틀린것..)
if start not in graph.keys():
    graph[start] = []

def DFS(start):

    need_visit = [start] # 스택...
    visited = []

    # 작은 수부터 탐색해야하므로, reverse sort...(스택을 사용해야하니 reverse sort)..
    for key in graph.keys():
        # graph[key].reverse()
        graph[key].sort(reverse=True)

    # DFS
    while need_visit:
        popped = need_visit.pop() # 팝...
        if popped not in visited:
            visited.append(popped)
            need_visit.extend(graph[popped])
            # if popped in graph.keys():        # 그런데 이렇게 쓸바에야 그냥 함수 첫부분에 쓰는게 낫겠다...
            #     need_visit.extend(graph[popped])

    # 결과 출력
    for data in visited:
        print(data, end = ' ')



def BFS(start):

    need_visit = [start] # 큐...
    visited = []

    # 작은수부터 탐색해야하므로, 리스트 sort...
    for key in graph.keys():
        graph[key].sort()

    # BFS
    while need_visit:
        popped = need_visit.pop(0) # 디큐...
        if popped not in visited:
            visited.append(popped)
            need_visit.extend(graph[popped])
            # if popped in graph.keys():   # 그런데 이렇게 쓸바에야 그냥 함수 첫부분에 쓰는게 낫겠다...
            #     need_visit.extend(graph[popped])
    # 결과 출력
    for data in visited:
        print(data, end = ' ')

# print(graph)
DFS(start)
print()
BFS(start)

# print()
# print("1 3 9 10 4 7 8 ")
# print("1 3 4 9 10 7 8 ")
exit()




# # 두번째 시도, 그냥 dict아닌 리스트로만 바꿔보자........역시 탈락 (로직에 문제가 있는듯...) >> 수정.... .reverse()가닌 sort(reverse=True)사용...
nv, ne, start = map(int, input().split())
graph = [[] for _ in range(1001)]
for _ in range(ne):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def printGraph(graph):
    for i in range(len(graph)):
        if len(graph[i]) > 0:
            print(i, graph[i])

def DFS(start):
    need_visit = [start] # 스택...
    visited = []

    # 작은 수부터 탐색해야하므로, reverse sort...(스택을 사용해야하니 reverse sort)..
    for array in graph:
        # array.reverse()
        array.sort(reverse=True)

    # DFS
    while need_visit:
        popped = need_visit.pop() # 팝...
        if popped not in visited:
            visited.append(popped)
            need_visit.extend(graph[popped])
    # 결과 출력
    for data in visited:
        print(data, end = ' ')



def BFS(start):
    need_visit = [start] # 큐...
    visited = []

    # 작은수부터 탐색해야하므로, 리스트 sort...
    for array in graph:
        array.sort()

    # BFS
    while need_visit:
        popped = need_visit.pop(0) # 디큐...
        if popped not in visited:
            visited.append(popped)
            need_visit.extend(graph[popped])
    # 결과 출력
    for data in visited:
        print(data, end = ' ')


DFS(start)
print()
BFS(start)

# 7 6 1
# 1 3
# 1 4
# 3 9
# 3 10
# 4 8
# 4 7


# 반례 인풋 ...외딴섬노드
# 5 4 1
# 2 3
# 3 4
# 4 5
# 5 2




# -----------------------


# 해답...dfs는 간단히 재귀적으로 구현. bfs는 큐(특히 deque)를 이용하여 구현...
from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)


#
# 소회
# :
#
# 0. 문제를 읽을때, 하나하나 놓치지 말고 보라
# 이번문제에선 "정범번호는 1번부터 N번까지다"라고 주어졌다(N은 그래프 상에서의 노드의 개수다)
# 만약 N=5라면, 노드의 번호는 1~5안에서 해결해야한다
# 그러므로 내가 수정했던 것처럼 굳이 10001길이의 리스트를 만들필요가 없었다.
#
# 1. dict()를 사용할땐 항상 조심하라.
# 3번째만에 합격하였다. 탈락한 이유는, 생각지도 못했던 반례가 있었기 때문이다
# 기껏 간선들을 이용해서 그래프를 만들었는데, 만약 왼딴 섬의 노드(간선이없는)가 존재한다면,
# 결국 내가 완성한 그래프는 비완성의 그래프가 된다.
# 게다가 나는 그래프를 dict()를 이용해서 만들었기때문에, 딕셔너리에 존재하지않는 키값으로 액세스하면 오류가 나기마련이다.
#
# 강사는 애초에 리스트를 이용해서 그래프를 구현했기때문에, 그럴위험이 없었다. dict()를 사용할땐 항상 주의해야겠다.
# 차라리 웬만하면 dict()보단 리스트를 위주로 사용하는게 낫겠다.
#
# 반례 인풋
# 5 4 1
# 2 3
# 3 4
# 4 5
# 5 2
# 반례 아웃풋
# 1
#
#
# 2.
# DFS,BFS를 구현할때 need_visit, visited 이 두가지의 리스트를 이용했는데, 강사의 코드는 조금 다르다
# 분석해보자.
# bfs는 아주간단히 재귀적으로 구현하였고, dfs는 내가 한것처럼 큐를 이용하였다.
# 특히 dfs는 내가 한것과 세가지 차이가 있다.
# 첫째, 그래프를 리스트로 구현
# -이건 문제특성상 노드의 개수가 N개일때, 노드의 번호는 1~N까지라고 미리 지정해줬기때문에 가능
# 둘째, visited를 불리언값의 리스트로 관리
# -이것도 첫번째의 이유와 동일하다. 리스트를 사용할 수가 있어서 공간복잡도에 부담이 없어졌다.
# 셋째, 큐를 일반 리스트가 아닌 collection라이브러리의 deque를 이용
# 리스트보다는 deque가 성능상의 이점이 있나? list().pop(0)보다는 deque.popLeft()가 낫나?
# >> 그렇다 "deque.popleft() is faster than list.pop(0), because the deque has been optimized to do popleft() approximately in O(1), while list.pop(0) takes O(n) (see deque objects)."
# >> 문서 참고요망: https://docs.python.org/2/library/collections.html#deque-objects
#
# 3.
# 기본적으로 DFS,BFS는 그냥 바로바로 코드가 나올정도로 외워야한다고 한다. 참고로 둘다 O(V+E)의 시간복잡도다!
#
#
#




