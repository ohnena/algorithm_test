#
# 백트래킹
# * 고려할 수 있는 모든 경우의 수 (후보군)를 상태공간트리(State Space Tree)를 통해 표현
# - 각 후보군을 DFS 방식으로 확인
# - 상태 공간 트리를 탐색하면서, 제약이 맞지 않으면 해의 후보가 될만한 곳으로 바로 넘어가서 탐색
#     Promising: 해당 루트가 조건에 맞는지를 검사하는 기법
#     Pruning (가지치기): 조건에 맞지 않으면 포기하고 다른 루트로 바로 돌아서서, 탐색의 시간을 절약하는 기법
#
# * 즉, 백트래킹은 트리 구조를 기반으로 DFS로 깊이 탐색을 진행하면서 각 루트에 대해 조건에 부합하는지 체크(Promising),
# 만약 해당 트리(나무)에서 조건에 맞지않는 노드는 더 이상 DFS로 깊이 탐색을 진행하지 않고, 가지를 쳐버림 (Pruning)


def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col: # 1차.수직 관계 체크...
            return False
        if abs(candidate[queen_row] - current_col) == current_row - queen_row: # 2차.대각선 관계 체크...
            return False
    return True


def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:]) # 깊은복사...
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()


def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result


print(len(solve_n_queens(8)))
# 예상결과: [[1, 3, 0, 2], [2, 0, 3, 1]]
