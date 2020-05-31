# 해답을 기반으로 DFS로 구현...

import sys
sys.setrecursionlimit(100000) # 이게 포인트...

def dfs(sx, sy):
    visited[sx][sy] = True
    for dx, dy in directions:
        x, y = sx+dx, sy+dy
        if(x<0 or x>= M) or (y<0 or y>=N): # 인덱스 범위 체크...
            continue
        if visited[x][y] == False and patch[x][y] == 1:
            dfs(x,y)

test_case = int(input())
for _ in range(test_case):
    M, N, K = map(int, input().split())
    patch = [[0]*N for _ in range(M)]
    visited = [[False]*N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        patch[x][y] = 1

    directions = [(1,0),(-1,0),(0,-1),(0,1)]


    count = 0
    for i in range(M):
        for j in range(N):
            if visited[i][j] == False and patch[i][j] == 1:
                count += 1
                dfs(i,j)

    print(count)


exit()

# 해답을 기반으로 BFS로 구현...
from collections import deque


def bfs(sx, sy):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    need_visit = deque([(sx, sy)])
    while need_visit:
        px, py = need_visit.popleft()
        if visited[px][py] == False:
            visited[px][py] = True
            for dx, dy in directions:
                x = px + dx
                y = py + dy
                if (x < 0 or x >= M) or (y < 0 or y >= N):  # 인덱스 범위 체크...
                    continue
                if visited[x][y] == False and patch[x][y] == 1:
                    need_visit.append((x, y))


test_case = int(input())
for _ in range(test_case):
    M, N, K = map(int, input().split())
    visited = [[False] * N for _ in range(M)]
    patch = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        patch[x][y] = 1

    count = 0
    for x in range(M):
        for y in range(N):
            if patch[x][y] == 1 and visited[x][y] == False:
                count += 1
                bfs(x, y)

    print(count)
    # exit()

exit()

# 1차 시도...완전히 갈피를 못잡고...망해버림....냄새를 조금 맡긴했는데, 구체적으로 DFS,BFS를 어떻게 적용할지가 어려웠음
# 그리고 결정적으로 문제 이해를 제대로 못했다ㅠㅠ. 애벌레가 상하좌우로만 움직일 수 있는 점도 그렇고, 최종적으로는 클러스터들의 수를 구해야한다는 것.
test_count = int(input())
for t in range(test_count):
    M, N, K = map(int, input().split())

    # 밭...
    patch = [[0] * N for _ in range(M)]
    can_cover = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        patch[x][y] = 1

        pos_x, pos_y = x - 1, y - 1
        if (pos_x >= 0 and pos_x < M) and (pos_y >= 0 and pos_y < N):
            can_cover[pos_x][pos_y] += 1
        pos_x, pos_y = x - 1, y
        if (pos_x >= 0 and pos_x < M) and (pos_y >= 0 and pos_y < N):
            can_cover[pos_x][pos_y] += 1
        pos_x, pos_y = x - 1, y + 1
        if (pos_x >= 0 and pos_x < M) and (pos_y >= 0 and pos_y < N):
            can_cover[pos_x][pos_y] += 1

        pos_x, pos_y = x, y - 1
        if (pos_x >= 0 and pos_x < M) and (pos_y >= 0 and pos_y < N):
            can_cover[pos_x][pos_y] += 1
        pos_x, pos_y = x, y
        if (pos_x >= 0 and pos_x < M) and (pos_y >= 0 and pos_y < N):
            can_cover[pos_x][pos_y] += 1
        pos_x, pos_y = x, y + 1
        if (pos_x >= 0 and pos_x < M) and (pos_y >= 0 and pos_y < N):
            can_cover[pos_x][pos_y] += 1

        pos_x, pos_y = x + 1, y - 1
        if (pos_x >= 0 and pos_x < M) and (pos_y >= 0 and pos_y < N):
            can_cover[pos_x][pos_y] += 1
        pos_x, pos_y = x + 1, y
        if (pos_x >= 0 and pos_x < M) and (pos_y >= 0 and pos_y < N):
            can_cover[pos_x][pos_y] += 1
        pos_x, pos_y = x + 1, y + 1
        if (pos_x >= 0 and pos_x < M) and (pos_y >= 0 and pos_y < N):
            can_cover[pos_x][pos_y] += 1
    print(patch)
    print(can_cover)

    cand = []
    for i in range(len(M)):
        for j in range(len(N)):
            if can_cover[i][j] > 0:
                cand.append([i, j, can_cover[i][j]])
    cand.sort(key=lambda data: data[2])

    popped = cand.pop()
    x, y = popped[0], popped[1]
    for data in cand:
        if (data[0], data[1]) in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                                  (x, y - 1), (x, y), (x, y + 1),
                                  (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]:
            exit()
