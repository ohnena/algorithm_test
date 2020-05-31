

# 그래프는 dict로 구현... (문제형태에 따라 리스트로 구현가능...)

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']



# dfs, bfs 구현....

def bfs(graph, start_node):  ### 강사왈...bfs정도는 알고리즘을 그냥 외우는것도 괜찮다고!!~~!
    visited = list()
    need_visit = list()  ## BFS의 구현은 이 2가지 큐가 있는게 포인트!!!

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)  # pop(0)하면 뒤에서 앞으로 채워져서...정말 큐의 pop한 효과!
        if node not in visited:  # not in...참 편하다!! 리스트를 뒤지는 방법!
            visited.append(node)
            need_visit.extend(graph[node])  # extend()...참편하구나!!

    return visited


def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()     # bfs에서 pop(0)으로 하면 신기하게 앞으로 땡겨졌지...dfs에선 pop()하면 맨뒤의 원소가 빠진다.(간편..)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

# 예상 입력1
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
#
# 예상 출력1
# 1 2 4 3
# 1 2 3 4

# 반례 인풋 #외짠섬 노드...
# 5 4 1
# 2 3
# 3 4
# 4 5
# 5 2
# 반례 아웃풋
# 1