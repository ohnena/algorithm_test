# 13.2 기타리스트
# 1495
# Medium
# 동적프로그래밍, 40분
# //지금까지 푼 동적프로그래밍 문제들은 모두 교과서적인 문제였다. 하지만 이번엔 실전문제다.
#
#
# 구상
# 동적프로그래밍 문제지만, 아이디어가 안떠올라서
# 재귀를 이용한 백트래킹을 구상해봤다 >> 역시...시간초과로 탈락...


# # 첫시도...재귀적으로 풀어봄.. >> 역시나 시간초과로 탈락...해설을 본다 ㅠㅠ
# max_vol = -1
# touch = False
# def recursive(value, index, VL, operand):
#     global max_vol
#     global touch
#     if index >= len(VL):
#         max_vol = max(max_vol, value)
#         touch = True
#         return
#     if operand == '+':
#         value += VL[index]
#     else:
#         value -= VL[index]
#     if value < 0 or value > M:
#         return
#     recursive(value, index + 1, VL, '+')
#     recursive(value, index + 1, VL, '-')
#
#
# N, S, M = map(int, input().split(' '))
# V = list(map(int, input().split(' ')))
# V = [0] + V
# max_vol = -1
# touch = False
# recursive(S, 0, V, '+')
#
# if touch == False:
#     max_vol = -1
# print(max_vol)
#
# #
# # import random
# # N, S, M = 3, 5, 10
# # V = [0]
# # V_list = [[0] for _ in range(100)]
# # for i in range(100):
# #     for _ in range(N):
# #         V_list[i].append(random.randint(1,10))
# #     max_vol = -1
# #     touch = False
# #     recursive(S, 0, V_list[i], '+')
# #     if touch == False:
# #         max_vol = -1
# #     print(V_list[i], max_vol)
#


# 해설을 보고나서 풀어본다.....원리는 굉장히 간단하다. 그래서 급하게 바로 짜보겠다...
# 1차 > 그냥 짜보기
# 2차 > 점화식에 맞춰서 수정
# 3차 > 탈락해서 살펴보니 마지막에 result를 0으로 두고 시작해서 문제... (노래출력이 안되는 최악의 경우에는 -1을 출력해야하는 조건이 있었지)

# 1 입력값 받기
N, S, M = map(int, input().split(' '))
V = list(map(int, input().split(' ')))
# N, S, M = 3, 5, 10
# V = [5, 3, 7]


# 2 DP용 테이블 세팅
V = [0] + V
D = [[False] * (M + 1) for _ in range(N + 1)]
D[0][S] = True

# 3 진행과정

# -D[i][j+1] = "i번째 노래일때 j크기의 볼륨으로 연주가능한지 여부
# //j+1인 이유는 해당 볼륨값을 그대로 index로 사용하기 위함이다.
# -점화식은,
# D[i][j-V[i]] = True (if D[i-1][j] = True)
# D[i][j+V[i]] = True (if D[i-1][j] = True)
for i in range(1, N+1):
    for j in range(M + 1):
        if D[i-1][j] == True:
            volume =  j - V[i]
            if  volume >= 0 and volume <= M:
                D[i][volume] = True
            volume = j + V[i]
            if volume >= 0 and volume <= M:
                D[i][volume] = True



# 4 결과 추출하여 출력하고 프로그램 종료
result = -1             # 주의! 출력못할때를 대비해 특정값을(-1) 문제에서 제시했다.
for volume in range(len(D[N])):
    if D[N][volume] == True:
        result = max(result, volume)

print(result)


# 소회
# :
# DP는 묘한 희열감이 있다. 그 풀이 진행과정을 시각적으로 보고 이해했을때 말이다. (그런 측면에서 01타일문제는 최악이다...시각적인 이해가 거의 불가능하달까?)
# 그래서인지 DP의 풀이는 테이블을 이용해 그 진행과정을 차근차근 update해 나가는 방식이 많은 것 같다. (물론 테이블이라고 해서 꼭 2차원 배열을 사용하진 않았지)
#
# 시각적 이해 이후에 그 과정을 점화식으로 압축해 넣는 게 중요하다. 그 점화식을 그대로 코드로 옮기게 될 수 있도록 말이다
#
# 또한 알고리즘 문제 특성상, 모든 조건에 만족하지 않을때 출력해야하는 값에 대해서도 문제에서 제시해주므로
# 마지막 결과 출력부분에서 그것을 놓치면 안되겠다
#
# 이번 '기타리스트' 문제에 대해서 조금 생각해보자면,
# DP의 특성상 이걸 어떻게 작은거에서 큰걸로 발전시켜나갈 수 있을까를 고민했다.
# 처음엔 자연스레 재귀를 떠올렸고 그렇게 구현해보기도 했다. 하지만 시간과 공간을 무지 잡아먹는 재귀에 대한 대안으로 종종 사용되는
# DP가 역시 이경우에도 나서야 할듯했다. 재귀로는 시간초과가 나서 탈락했기때문이다. (그럴거 알면서 왜 재귀로 짰니...바보 그냥 호기심이긴했다..)
#
# 그렇다면 DP로 이걸 어떻게 풀어야할까?
# 이전의 기본 DP문제에서 처럼 memorization을 위해 테이블을 이용해봐야겠다. 대부분 테이블을 이용해서 진행과정을 구상하더라
# 그런데 테이블에 어떤 정보를 점증적으로 발전시켜가야할까?
#
# 우선 주어진건 시작 볼륨인 5이고, 매노래마다 조정하는데 사용되는 볼륨변화값이 [5,3,7]로 주어졌다.
# 그리고 그걸 적용해서 계산된 볼륨값에 대한 허용범위가 0~10으로 주어졌다
#
# 그럼 매턴이 5->3->7로 볼 수 있으니 테이블의 row는 5,3,7로 잡고,
# 테이블의 column은 뭐로 잡아야할까? (이부분이 이 알고리즘의 kick이다!)
#
# 두괄식으로 답부터 얘기하자면, 0~10의 허용범위를 컬럼으로 잡는다
# 그리하여 5의 turn에선, 이전 turn의 결과볼륨에 5의 볼륨변화값을 적용했을때, 허용범위에든 볼륨들을 체크해두는 것이다.
# (모두 False로 세팅한후, 허용범위에 들면 True로 바꾼다든지 하는 방식으로 말이다.)
#
# 테이블(진행과정)의 row와 column을 결정하여 원리를 구상해냈으니, 점화식만 만들면된다
# 점화식은 아무래도 거의 그대로 코드로 옮겨질테니 깔끔하게 만들자.
#
# 점화식만 만들면, 코딩은 시간문제다.
#
# //마지막으로 주의할건, 문제에선 출력값이 존재하지 않거나 허용범위를 너무 넘어버렸을때는 어떤특정값을 출력하라고 할때가 많으니 그부분을 놓치지 말자!
#
# 하아....이렇게나 reasonable하게 좀 풀어봤는데, 이것도 결국 해설강의를 보고나서 생각하는 거다. 결국 한계에서 벗어나지 못하고 있는 것이라 좌절이다.
# 그래도 힘내자!