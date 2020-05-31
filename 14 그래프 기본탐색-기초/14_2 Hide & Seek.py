#
#
#
# 구상
# :
#
# 시작점으로부터, 매 레벨마다 3개의 분기가 나오는 3진트리로 구상.
# 단 매 3개의 분기는 -1,+1,*2의 결과를 노드로 갖는다.
# 노드는 (값,트리의 레벨)의 구조를 갖는다. 트리의 레벨의 경과시간이라고 볼 수 있기때문이다.
# ex) 시작노드 (5,0)
# (5-1,1)   (5+1,1)   (5*2,1)
# ...
#
# BFS를 이용한다. 미래를 예측할 수 없기때문에, 한가지 확실한건 DFS보다는 BFS가 그나마 안전하다는 것
#
#






# 해답....결국 실패했다. 일반 visited 개념을 사용했더니 성능이슈를 커버하지 못한다. (또한 DP의 개념도 살짝 첨가했다)
# 결국 해답은 visited 구현에서 갈리는 문제다. 여기선 visited[숫자]=경과시간으로 구현해서 문제를 해결한다.
# 특히 미리 visited = [0] * 100001로 세팅해두는 것에서부터 심플함을 자랑한다.
# 또한 visited[next_pos] = visited[now_pos] + 1로 계산하듯이, 이전의 값을 이용해서 계속 업데이트 해나간다.
# 이는 마치 다이나믹 프로그래밍을 닮았다.
from collections import deque

MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2): # 신기한 문법...
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1 # 마치 DP를 보는듯...
                q.append(next_pos)

print(bfs())
exit()

# 두번째 시도....강사로부터 얻은 힌트...visited를 도입...+그래도 프로그램이 종료할 생각을 안해서
# 그래도 0 100000는 너무 오래걸려서, visited에 check_location()까지 모두 도입...

from collections import deque


def check_location(point):  # 사용 보류...
    if point >= 0 and point <= 100000:
        return True
    else:
        return False


def bfs(start, dest):
    # 동일한지 체크...
    if start == dest:
        return 0

    visited = []
    need_visit = deque([])

    if check_location(start - 1):
        need_visit.append((start - 1, 1))
    if check_location(start + 1):
        need_visit.append((start + 1, 1))
    if check_location(start * 2):
        need_visit.append((start * 2, 1))

    i = 0
    while need_visit:
        popped = need_visit.popleft()
        number = popped[0]
        time = popped[1]
        visited.append(number)

        # 한계 체크...
        # if popped[0] < 0 or popped[0] > 100001:
        #     continue

        # 연산시작...

        if (number - 1) == dest:
            # print(need_visit)
            return time + 1
        else:
            if check_location(number - 1) and (number - 1) not in visited:
                # if (popped[0] - 1) not in visited:
                need_visit.append((number - 1, time + 1))

        if (number + 1) == dest:
            # print(need_visit)
            return time + 1
        else:
            if check_location(number + 1) and (number + 1) not in visited:
                # if (popped[0] + 1) not in visited:
                need_visit.append((number + 1, time + 1))

        if (number * 2) == dest:
            # print(need_visit)
            return time + 1
        else:
            if check_location(number * 2) and (number * 2) not in visited:
                # if (popped[0] * 2) not in visited:
                need_visit.append((number * 2, time + 1))

        # print(len(need_visit), len(visited), popped, i)
        i += 1
        if i > 600000:
            return -1


start, dest = map(int, input().split())
print(bfs(start, dest))
exit()

# 첫 시도...직접 짜봤는데...자신있게 제출했다가 광탈...이후 3번정도 수정했는데 광탈...성능의 벽을 못넘음...
# 0 100000 입력시 루프가 백만번을 훌쩍 넘어버림..
from collections import deque


def check_location(point):  # 사용 보류...
    if point >= 0 and point <= 100000:
        return True
    else:
        return False


def bfs(start, dest):
    # 동일한지 체크...
    if start == dest:
        return 0

    need_visit = deque([])
    need_visit.append((start - 1, 1))
    need_visit.append((start + 1, 1))
    need_visit.append((start * 2, 1))

    i = 0
    while need_visit:
        popped = need_visit.popleft()

        # 한계 체크...
        if popped[0] < 0 or popped[0] > 100001:
            continue

        # 연산시작...

        if (popped[0] * 2) == dest:
            # print(need_visit)
            return popped[1] + 1
        else:

            need_visit.append((popped[0] * 2, popped[1] + 1))

        if (popped[0] - 1) == dest:
            # print(need_visit)
            return popped[1] + 1
        else:

            need_visit.append((popped[0] - 1, popped[1] + 1))

        if (popped[0] + 1) == dest:
            # print(need_visit)
            return popped[1] + 1
        else:

            need_visit.append((popped[0] + 1, popped[1] + 1))

        i += 1
        if i > 1000000:
            return -1


start, dest = map(int, input().split())
print(bfs(start, dest))
