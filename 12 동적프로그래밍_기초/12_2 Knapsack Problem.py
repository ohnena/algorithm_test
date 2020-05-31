#
# # 직접짜보았다...."틀렸습니다"...탈락 OTL....
# N, K = map(int, input().split(' '))
# dp = [0] * 100001
#
#
# for _ in range(N):
#     w, v = map(int, input().split(' '))
#     dp[w] = v
#
# for j in range(0, K+1):
#     max = 0
#     for i in range(0, j + 1):
#         if i == (j - i):
#             continue
#         value = dp[i] + dp[j - i]
#         if value > max:
#             max = value
#     dp[j] = max
#
# print(dp[K])
#


# 슬럼프 후에, 다시 직접 짜보았다. (강의 보고나서) ... 성공!!
# input_list = [[], [6, 13], [4, 8], [3, 6], [5, 12]]
# N, K = 4, 7 # input()...
N, K = map(int, input().split(' '))
MV = [[0] * (K + 1) for _ in range(N + 1)]  # Array for Max Value
for turn in range(1, N + 1):
    # w, v = input_list[turn] # need to be advised with input()...
    w, v = map(int, input().split(' '))
    for k in range(1, K + 1):
        # if w > k:
        #     new_v = MV[turn-1][k]
        # else:
        #     new_v = MV[turn-1][k-w] + v
        #
        # # if new_v > MV[turn-1][k]:
        # #     MV[turn][k] = new_v
        # # else:
        # #     MV[turn][k] = MV[turn-1][k]
        # MV[turn][k] = max(new_v, MV[turn-1][k])
        if w > k:        # 마치 점화식형태로 깔끔하게 떨어지네...
            MV[turn][k] = MV[turn - 1][k]
        else:
            MV[turn][k] = max(MV[turn - 1][k], MV[turn - 1][k - w] + v)

print(MV[N][K])
# print(MV)

exit()



# 해답...
# 1 입력값을 받는다
N, K = map(int, input().split(' '))

# 2 2차원 배열을 초기화한다
dp = [[0] * (K + 1) for i in range(N + 1)]

# 3 점화식을 적용한다.
for i in range(1, N + 1):
    weight, value = map(int, input().split(' '))
    for j in range(1, K + 1):
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

# 4 최종turn N에서의 허용무게 K에 대한 최대가치를 출력하고 프로그램을 종료한다.
print(dp[N][K])



# 소회
# :
# 1)
#
# 이번 Knapsack문제는 다이나믹프로그래밍의 단골 문제라고 한다. 그렇기때문에 기억이 날때까지 반복해서 반복해서 풀어보고 숙달하라고!!!
# 그런데 의외로 이문제가 (처음본사람에게) 까다로운건 피보나치수열때처럼 팬앤노트 시뮬레이션 전에 점화식이 나오는 그런 케이스가 아니기때문이다
# 즉 피보나치수열처럼 문제에 손대기전부터 점화식이 깔끔하게 떨어지는 유형이 아니라는말.
# 특히나 이번건 table(2차원배열)로 memorization을 하기때문에 index처리하는 부분이 까다롭다. 그러므로 팬엔노트 시뮬레이션이 필수라고 생각된다
# (고백하자면, 피보나치수열도 쉬운 점화식에 비해 구현이 직관적이진 않았던듯하다...OTL...그런데 신기하게 이 Knapsack문제는 구현에서 점화식을 바로 사용한다...깔끔..
# 점화식은 깔끔하지 않은데, 구현은 점화식을 그대로 사용하면되는 형태랄까?....ㅋㅋ 해놓고보니 뭔소린지...)
#
# 2) //이후의 내용은 아래의 강의메모로 대체한다
#
# <슬럼프를 극복하기위해 다시 시작한다! ㅋㅋ>
# Knapsack문제부터 다시 강의를 보자.
#
# 우선 다이나믹프로그래밍에 관하여 복기해보자면,
# 그 특징은 2가지로 좁혀볼 수 있다. 첫째는 Memorization을 이용한다는 점이고(그 점에서 D&C와 다르지), 두번째는 점화식이 필요하다는 것이다.
# 피보나치수열이 바로 다이나믹프로그래밍의 대표적 문제인데, 보통은 재귀적으로 푸는걸 먼저 생각하는게 자연스럽지만, 고수들은 다이나믹프로그래밍으로 푼다!
# (메모리측면이나 속도의 문제 때문이겠지?)
#
# 어쨌든 이러한 다이나믹프로그래밍의 특징을 기반으로 Knapsack문제를 풀어보자.
# 풀이법이 몇가지 있다고하는데, 여기서는 table을 이용한 방식을 사용한다.
#
# 우선 우리의 목표는 "최대가치값(무게7)"을 구하는 것이다.
# 사실 다이나믹프로그래밍인 만큼, memorization을 위해 최대가치값(무게1), 최대가치값(무게2), ..., 최대가치값(무게6)을 기억해놔야할 것이다. (ㅋㅋ 뇌속의 문제해결의 순서가 잘못되긴했다만) 물론 이게 피보나치때처럼 점화식의 그림이 깔끔하게 떨어지진 않는다.
#
# 참고) 굳이 점화식을 적어보자면... (물론 직관적이진 않다)
# MV[turn][k] =
# if w > k:
#   MV[turn-1][k]
# else:
#   max(MV[turn-1][k], MV[turn-1][k-w] + v
# //여기서 w,v는 매턴의 input값. 즉 매턴마다 입력받은 item 하나의 무게와 가치.
#
#
# *주목!) 이 Knapsack문제는 정말 단골 문제라서, 완전히 익숙해질때까지 반복해서 풀어봐서 꼭 숙달하라고!