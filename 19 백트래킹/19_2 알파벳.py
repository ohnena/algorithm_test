# BOJ 1987


# 소회
# :
# 세번만에 성공했다. 아으 힘들어라.
#
# 첫번째 실패이유는, 백트래킹을 재귀DFS로 구현해서 시간초과가 났기때문이다. 그래서 해답을 참고했더니 BFS로 했더라.
# 두번째 실패이유는, BFS로 구현하긴했는데, 메모리 초과가 났다. 그냥 기존하던대로 우선순위큐 구현을 위해 dequeue를 썼는데, 아마도 이 문제인 듯 하다.
#             중복데이터가 꽤 있는듯.
# 세번째 실패이유는, 해답을 완전히 참고하여 BFS+(우선순위큐를 set으로 구현) // 사실 구현로직상 큐인지 스택인지는 중요하지 않구나....그래서 set()을 이용
#
# 특이한건, PyPy3에선 7초걸리고, Python3에선 2초쯤걸렸다


## 세번째 시도 >> 두번째 시도 코드 + dequeue를 set을 바꿨다... >> set을 사용하는 이유를 배웠다.
R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input())


directions = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(start_r,start_c):

    q = set()
    q.add((start_r, start_c, board[start_r][start_c]))
    while q:
        current_r, current_c, current_chars = q.pop()
        max_steps = max(max_steps, len(current_chars))
        for d in directions:
            next_r = current_r + d[0]
            next_c = current_c + d[1]
            if (next_r >= 0 and next_r < R) and (next_c >= 0 and next_c < C) and (board[next_r][next_c] not in current_chars):
                q.add((next_r,next_c,current_chars+board[next_r][next_c]))

    return max_steps

print(bfs(0,0))



exit()
## 두번째 시도 >> 해답기반 BFS... >> 메모리 초과로 광탈... (아...해답대로 dequeue가 아닌 set으로 해보자)
R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(input())




from collections import deque

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(start_r,start_c):

    max_steps = 0
    q = deque([(start_r, start_c, board[start_r][start_c])])
    while q:
        current_r, current_c, current_chars = q.popleft()
        max_steps = max(max_steps, len(current_chars))
        for d in directions:
            next_r = current_r + d[0]
            next_c = current_c + d[1]
            if (next_r >= 0 and next_r < R) and (next_c >= 0 and next_c < C) and (board[next_r][next_c] not in current_chars):
                q.append((next_r,next_c,current_chars+board[next_r][next_c]))

    return max_steps

print(bfs(0,0))












exit()
## 첫시도 >> 시간초과로 광탈... 그렇다면 BFS로 다시 구현해보자. (다만 해답을 기준으로...)

# 1 입력
R, C = map(int, input().split())
visited = [[False]*C for _ in range(R)]
board = [[] for _ in range(R)]


for i in range(R):
    s = input()
    # for j in range(len(s)):
    for c in s:
        board[i].append(c)


# 2 검증함수 구현
def is_available(row,col, history):
    if (row < 0 or row >= R) or (col <0 or col >= C): # 좌표 허용범위 체크
        return False
    if visited[row][col] == True: # 방문 여부 체크
        return False
    if board[row][col] in history: # 알파벳 중복 체크
        return False
    return True


# 3 검증함수를 사용하여 dfs구현
directions = [(1,0),(-1,0),(0,1),(0,-1)]
max_steps = 0
def dfs(current_row, current_col, current_step, history):
    global max_steps
    max_steps = max(current_step, max_steps)

    visited[current_row][current_col] = True
    history.append(board[current_row][current_col])
    for d in directions:
        row = current_row + d[0]
        col = current_col + d[1]
        if is_available(row, col, history):
            dfs(row, col, current_step+1, history)
            visited[row][col] = False
            history.pop()


# 4 백트래킹 실행하여 결과 출력후 종료
dfs(0,0,1,[])
print(max_steps)