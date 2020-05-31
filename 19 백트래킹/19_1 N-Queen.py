# 조건 1<=N<=15


# 백트래킹 3총사
# def is_available(candidate_cols, current_col):
# def dfs(N, current_col, candidate_cols, final_result): # 재귀, 깊은복사 주의...
# def solve_n_queen(N):


# 실화냐?...N<=15인 것을 악용한 ㅋㅋ...
print([0,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596][int(input())])
exit()






# 소회
# :
# 복습을 통해 백트래킹 코딩을 다시 해보았다. state space tree로 각 stage를 관리하고, 그것을 재귀적 DFS를 통해
# 순회한다. DFS과정에서 PROMISING(조건에 맞는지)과 PRUNING(빽치기)을 처리한다.
#
# N-Queen문제의 핵심은 이전에 놓인 퀸들과의 수직관계, 대각선관계 이 두가지 체크를 통과해야 다음 퀸으로 놓일 수 있다는 것이다.
#
# 해답 코드의 특이한점은 복습한 코드처럼 candidate_cols를 리스트로 주렁주렁 가지고 다니지 않으니,
# 굳이 PRUNING을 코드상에 명시할 필요없다는 점이다. 복습한 코드에선 재귀에서 돌아왔을때 pop()을 해서(PRUNING),
# 새로운 컬럼을 PROMISING 하도록 했다. 하지만 해답코드에서는 pop()할필요없이 그냥 column[current_row] = current_col 이런식으로
# 값을 덮어써버리면 그만이었다.
#
# 요약하자면, 해답코드의 단점은 기존코드코다 덜 직관적인 점이지만, 장점은 구현의 복잡도는 줄었다는 것이다.





# 해답...
def is_available(current_row):
    for queen_row in range(current_row):
        # 수직관계 체크
        if column[queen_row] == column[current_row]:
            return False
        # 대각선관계 체크
        if current_row - queen_row == abs(column[queen_row] - column[current_row]):
            return False
    return True


def dfs(current_row):
    global result
    if current_row == N:
        result += 1
        return

    for current_col in range(N):
        column[current_row] = current_col # PRUNING...(?)
        if is_available(current_row): # PROMISING...
            dfs(current_row + 1)


N = int(input())
column = [0] * N
result = 0
dfs(0)
print(result)







exit()
## 최초시도...PyPy3로 30초로 간신히 합격...(하지만 성능은...OTL)
n = int(input())

def is_available(candidate_cols, current_col):
    current_row = len(candidate_cols)
    for queen_row in range(len(candidate_cols)):
        # 수직관계 체크
        if candidate_cols[queen_row] == current_col:
            return False
        # 대각선관계 체크
        if (current_row - queen_row) == abs(candidate_cols[queen_row] - current_col):
            return False
    return True



def dfs(N, current_row, candidate_cols, final_result):
    if current_row == N:
        final_result.append(candidate_cols[:]) # 깊은 복사...
        return
    for current_col in range(N):
        if is_available(candidate_cols, current_col): # << PROMISING >>
            candidate_cols.append(current_col)
            dfs(N, current_row + 1, candidate_cols, final_result) # 재귀...
            candidate_cols.pop() # << PRUNING >>

def solve_n_queen(N):
    final_result = []
    dfs(N, 0, [], final_result)
    return final_result


print(len(solve_n_queen(n)))