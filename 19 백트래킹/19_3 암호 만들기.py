# BOJ 1759




# 소회
# :
# 첫시도를 재귀dfs로 했는데... 구현자체를 실패했다. 괜히 머리좀 써보려고했다가, 혼돈의 카오스로 가버렸다.
# 아무래도 최적화는 나중에 신경쓰고, 첫구현때는 아이디어만 최대한 빨리 실현하는 방향이 맞겠다.
#
# 두번째 시도에선 BFS를 기반으로 다시 만들었다.
# 지금와서 생각하니, BFS이든 DFS이든 이름신경을 안쓰게 된다. 그냥 그 원리와 코드를 매핑시키지 그 사이의 '이론'을 생각안하게 된다.
# 특히 이번 문제에선 DFS,BFS는 전자는 재귀, 후자는 큐라는 생각으로만 구현했다.
# 그렇다고 틀렸다는 건 아니다. 다만 이렇게 DFS와 BFS가 익숙해져 갈 정도로, 별거 아닌거라는 생각이 들뿐이다.
# (두번째 시도에서도 자음,모음 체크를 깜박해서 괜히 좌절했는데....결국 좌절하는게 맞긴하지. 문제에서 준 조건자체를 놓쳐버렸다...)
#
# 세번째 시도에선 처음 시도한 재귀dfs를 소생시켜보았다. 다시 풀어보니 무진장 간단했다. (OTL...)
# 보통 DFS(next_index, result)를 재귀로 진입할때, result에 next_index에 해당하는 내용이 포함시켜서 들어갈지
# 고민을 했다. 처음 실패한 이유는 포함을 안하고 들어가서였다. 어쩐지 index가 자꾸 씹혀서 고민하다가 혼란스러워졌었다. 이 힌트는 사실
# BFS구현때 얻은 거다. BFS때도 똑같이 큐에 append할때 (next_index, result)에서 result에 next_index의 내용을 포함안시키고 했더니,
# 계속 인덱스문제가 생겼더랬다.
#
# 결론은 DFS,BFS를 할때, 큐에넣든 재귀로진입하든간에, 이렇게 q.append(next_index, result) 혹은 dfs(next_index, result)
# 하는게 낫다는 것이다. (우선은 그러하다...하하 삽질을 막기위한 그냥 팁이랄까?)
#
#
# 참고) 파이썬 comibination라이브러리를 이용한 코드도 신박하더라...대신 백트래킹 구현을 안한다는 함정(?)이...



# dfs 재귀로 빠르게 풀어보자




# 해답1 파이썬 comibindation 라이브러리 이용... (백트래킹 사용 No...)
from itertools import combinations

vowels = ('a','e','i','o','u')
L, C = map(int, input().split())

array = input().split()
array.sort()
for password in combinations(array, L): # 6C4의 조합 결과를 출력하는 구나...
    v_count = 0
    for i in password:
        if i in vowels:
            v_count += 1

    if v_count >= 1 and (len(password)-v_count >= 2) :
        print(''.join(password)) # 신기한 스트링의 메소드...










# 해답2..DFS사용한 백트래킹...
# deepcopy를 사용하는 거 보니, 재귀dfs를 이용한 전형적인 백트래킹 구현법이다...
import copy

result = []
string = []
visited = []

# 조합(Combination) 함수 구현
def combination(array, length, index):
    # 길이가 length인 모든 조합 찾기
    if len(string) == length:
        result.append(copy.deepcopy(string))
        return
    # 각 원소를 한 번씩만 뽑도록 구성
    for i in range(index, len(array)):
        if i in visited:
            continue
        string.append(array[i])
        visited.append(i)
        combination(array, length, i + 1)
        string.pop()
        visited.pop()

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split(' '))

# 가능한 암호를 사전식으로 출력해야 하므로 정렬 수행
array = input().split(' ')
array.sort()

combination(array, l, 0)

# 길이가 l인 모든 암호 조합을 확인
for password in result:
    # 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1

    # 최소 한 개의 모음과 최소 두 개의 자음이 있는 경우 출력
    if count >= 1 and count <= l - 2:
        print(''.join(password))











#두번째 시도 >> BFS로 겨우 성공...
L, C = map(int, input().split())

candidates = list(input().split())
candidates.sort()


def check(chars):
    aa = ['a','e','i','o','u']
    j_count = 0
    m_count = 0
    for c in chars:
        if c in aa:
            m_count += 1
        else:
            j_count += 1
        if m_count >= 1 and j_count >= 2:
            return True
    return False


from collections import deque
def bfs():
    q = deque([])
    for i in range(C-(L-1)):
        q.append((i, candidates[i]))
    while q:
        current_i, current_chars = q.popleft()
        if len(current_chars) == L:
            if check(current_chars): # 자음, 모음 체크...
                print(current_chars)
            continue
        for next_i in range(current_i+1, C):
            q.append((next_i, current_chars + candidates[next_i])) # candidates[next_i]를 포함시켰다..


bfs()






## 세번째시도 >> 소생성공...
## 첫시도 >> dfs 구현자체를 실패...OTL...


L, C = map(int, input().split())

candidates = list(input().split())
candidates.sort()


def dfs(current_i, current_chars):
    if len(current_chars) == L:
        if check(current_chars):
            print(current_chars)
        return
    for next_i in range(current_i + 1, C):
        dfs(next_i, current_chars + candidates[next_i]) # candidates[next_i]를 포함시켰다..


def check(chars):
    aa = ['a','e','i','o','u']
    j_count = 0
    m_count = 0
    for c in chars:
        if c in aa:
            m_count += 1
        else:
            j_count += 1
        if m_count >= 1 and j_count >= 2:
            return True
    return False


for i in range(C-(L-1)):
    dfs(i, candidates[i])