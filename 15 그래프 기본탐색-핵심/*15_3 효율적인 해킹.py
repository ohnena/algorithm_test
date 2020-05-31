#
# 15.3 효율적인 해킹
# 1325
# easy, DFS, BFS, 30분


# 구상
# :
# BFS로 짜려고한다. V<=1만, E<=10만이므로, 재귀를 이용한 DFS는 부담스럽다.
# 주의할건, 방향그래프라는 것이다. 또한 신뢰관계에 따라, 입력값의 반대방향으로 방향이 주어진다.
# 그것에 주의해서 그래프를 생성하자



# 이유는 모르겠지만, 시간초과가 뜨거나 채점진행이 안되는문제...백준사이트 서버가 문제인가? 우선 PASS하자.


# 1 입력받기 및 graph, visited등 필요한 것들 세팅.
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    trusted, trust = map(int, input().split())
    graph[trust].append(trusted)
visited = [False] * (V + 1)

# 2 BFS함수 정의,구현
from collections import deque

def bfs(start):
    count = 0
    # visited = [False] * (V + 1)
    need_visit = deque([start])
    while need_visit:
        popped = need_visit.popleft()
        visited[popped] = True
        count += 1
        for next in graph[popped]:
            if visited[next] == False:
                need_visit.append(next)
    return count

# 3 BFS함수를 사용하여 가장많이 해킹하는 컴퓨터목록 얻기

result = []
for i in range(1, V+1):
    visited = [False] * (V + 1)
    count = bfs(i)
    result.append((i,count))
max_count = 0
for data in result:
    max_count = max(max_count, data[1])
com = []
for data in result:
    if data[1] == max_count:
        com.append(data[0])

com.sort()
for i in com:
    print(i, end= ' ')
