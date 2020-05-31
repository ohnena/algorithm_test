# 8.5 성 지키기
# 1236
# easy, 탐색, 20분


# 문제
# 영식이는 직사각형 모양의 성을 가지고 있다. 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다. 영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.
#
# 성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 성의 세로 크기 N과 가로 크기 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 성의 상태가 주어진다. 성의 상태는 .은 빈칸, X는 경비원이 있는 칸이다.
#
# 출력
# 첫째 줄에 추가해야 하는 경비원의 최솟값을 출력한다.


# //인풋
# 4 4
# ....
# ....
# ....
# ....

# //아웃풋
# 4




# <<< TEST CODE >>> Start...
N, M = 4, 4
L = []

L.append(list("...."))
L.append(list(".X.."))
L.append(list("..XX"))
L.append(list("...."))

answer = 0

# print("---------")
# for a in L:
#     print(a)


def castleDefense(N,M,L):




    guards = []


    # 경비 찾기...
    for n in range(N):
        for m in range(M):
            if L[n][m] == 'X':
                guards.append((n,m))

    # 직접짠...잘못된 알고리즘....
    #
    #
    # guard_cands = []
    # # 경비가 커버하는 구역 모두 X체크...
    # for r, c in guards:
    #     for n in range(N):
    #         for m in range(M):
    #             if n == r or m == c:
    #                 L[n][m] = "X"
    #
    # # 경비후보 찾기...
    # for n in range(N):
    #     for m in range(M):
    #         if L[n][m] != "X":
    #             guard_cands.append((n, m))
    #
    #
    # # 후보배치하면서 카운트해보기...
    # count = 0
    # new_guard_cands = []
    #
    # for r, c in guard_cands:
    #     if L[r][c] == "X":
    #         continue
    #     for n in range(N):
    #         for m in range(M):
    #             if n == r or m == c:
    #                 L[n][m] = "X"
    #     count += 1
    #
    # return count

    row = {} #dictionary
    col = {}
    row_count = 0
    col_count = 0

    # dictionary 세팅...
    for i in range(N):
            row[i] = 0
    for i in range(M):
            col[i] = 0

    # 경비 찾기...
    for n in range(N):
        for m in range(M):
            if L[n][m] == 'X':
                guards.append((n,m))

    # 커버되는 row,col 체크...
    for g in guards:
        row[g[0]] = 1
        col[g[1]] = 1

    # 커버되지 않는 row,col수 구하기...
    for i in range(len(row)):
        if row[i] == 0:
            row_count += 1
    for i in range(len(col)):
        if col[i] == 0:
            col_count += 1

    # 결과 리턴.
    if row_count > col_count:
        return row_count
    else:
        return col_count





print(castleDefense(N,M,L))
exit(0)
assert castleDefense(N,M,L) is answer


# <<< TEST CODE >>> End...





N, M = map(int, input().split(' '))
L = []
for _ in range(N):
    string = str(input())
    L.append(list(string))
print(castleDefense(N,M,L))








# # 제출
#
#
#
# def castleDefense(N,M,L):
#
#     guards = []
#     row = {} #dictionary
#     col = {}
#     row_count = 0
#     col_count = 0
#
#     # dictionary 세팅...
#     for i in range(N):
#             row[i] = 0
#     for i in range(M):
#             col[i] = 0
#
#     # 경비 찾기...
#     for n in range(N):
#         for m in range(M):
#             if L[n][m] == 'X':
#                 guards.append((n,m))
#
#     # 커버되는 row,col 체크...
#     for g in guards:
#         row[g[0]] = 1
#         col[g[1]] = 1
#
#     # 커버되지 않는 row,col수 구하기...
#     for i in range(len(row)):
#         if row[i] == 0:
#             row_count += 1
#     for i in range(len(col)):
#         if col[i] == 0:
#             col_count += 1
#
#     # 결과 리턴.
#     if row_count > col_count:
#         return row_count
#     else:
#         return col_count
#
#
#
#
#
# N, M = map(int, input().split(' '))
# L = []
# for _ in range(N):
#     string = str(input())
#     L.append(list(string))
# print(castleDefense(N,M,L))

#
# # 소회
# - 몇시간동안 삽질했다...문제를 잘못이해했기때문.
# - 문제에서는 커버되지 않는 row, col을 기준으로 답을 구해야했는데,
# - 나는 커버되지 않는 space를 기준으로 답을 구했다.... OTL....
# - 어쨌든 커버되지 않는 row와 col의 수 중에 더 큰것을 답으로 선택하는게 인상적...

