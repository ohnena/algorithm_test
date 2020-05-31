#
#
#
# 구상
# 1 준비사항
# -그래프완성 //간단한게 리스트 내 리스트로 가자 ex) graph[1] = [2,5]
# -BFS,DFS모두 가능하니, 간단히 큐로 만드는 BFS로 해보자. 그러므로 visited가 필요한데, visited를 boolean값의 리스트로 만들자
# 2 BFS 구현
# -count를 하나 변수로 둬서, visited[x] = True할때마다 1씩 increment하면 될듯 ...

from collections import deque

nv = int(input())
ne = int(input())
graph = [[] for _ in range(nv + 1)]
for _ in range(ne):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)




def bfs(graph, start):
    need_visit = deque([start])

    count = -1
    while need_visit:
        popped = need_visit.popleft()
        if visited[popped] == False:
            count += 1
            visited[popped] = True
            for v in graph[popped]:
                need_visit.append(v)
    print(count)



# bfs실행
visited = [False] * (nv + 1)
bfs(graph, 1)





# <이런문제는 DFS로 풀어야 제맛!>
#
# 강사에 따르면 노드의 개수가 100개이하로 파이썬의 재귀리미트를 벗어나지 않을 그래프이므로,
# 그냥 DFS를 재귀적으로 구현해서 빠르게 풀어란다. 코드가 BFS보다 훨씬 짧고 간단하다는 장점때문이다. (그렇지 않다면 BFS를 선호하겠지만..)
dfs_count = -1
def dfs(graph, start):
    global dfs_count
    dfs_count += 1
    visited[start] = True
    for node in graph[start]:  # 이러한 DFS 코드 형태를 반드시 기억하자. visited=true로 바꾸고, 거기에 달린 노드중 아직 방문안한 녀석들에 재귀적으로 접근.
        if visited[node] == False:
            dfs(graph, node)

# dfs실행
visited = [False] * (nv + 1)
dfs(graph, 1)
print(dfs_count)



