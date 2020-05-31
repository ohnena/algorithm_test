# 복습차원에서 다시 펜엔노트 시뮬 후, 코딩 해본다.

# D[i] = "수열의 i번째 원소를 끝으로 하는 부분수열의 최장 길이"
# D[i] = max(D[i], D[j]+1) if S[i] > S[j] (0 <= j < i)

# 예상 인풋
# 6
# 10 20 10 30 20 50
# 예상 아웃풋
# 4

# 복습시 2차 코드 - 제출 합격!
N = int(input())
S = list(map(int, input().split()))
D = [1] * (N)          # 처음에 모두 1로 초기화하는게 포인트구나!
for i in range(N):
    for j in range(i):
        if S[j] < S[i]:
            D[i] = max(D[i], D[j] + 1)
print(max(D))
exit()



# 복습시 최초 코드...처음에 D를 모두 0으로 초기화 했다가 애먹었다...1로 초기화해야한다.
N = int(input())
S = list(map(int, input().split()))
S = [0] + S
D = [0] * (N + 1)
print('S', S)
for i in range(N + 1):
    for j in range(i):
        if S[j] < S[i]:
            D[i] = max(D[i], D[j] + 1)
    print(i, D)

exit()

# 12_3 Longest Increasing Subsequence
# 가장 긴 증가수열
#
#
#
#

# 1차시도....살패...
# # 펜노트 시뮬레이션 ex)
# N = int(input())
# input_list = list(map(int, input().split(' ')))
input_list = [10, 20, 10, 30, 20, 50]
N = len(input_list)

max_len = 0
max_index, max_value = 0, 0
# 인덱스0의 값 10까지의 최장거리 max_len은? 시작점이므로 바로 max_len++. 거기까지의 max_index,max_value 업데이트 = (0, 10) // 1,0,10
# 익덱스1의 값 20까지의 최장거리 max_len은? 20>max_value이므로, max_len++하고 max_index,max_value 업데이트 //2,1,20
# 인덱스2의 값 10까지의 최장거리 max_len은? 10>max_value가 아니므로, max_len, max_index, max_value 그대로... //2,1,20
# 인덱스3의 값 30까지의 최장거리 max_len은? 30>max_value이므로, max_len++하고 max_index,max_value 업데이트... //3,3,30
# 인덱스4의 값 20까지의 최장거리 max_len은? 20>max_value가 아니므로, max_len, max_index, max_value 그대로... //3,3,30
# 인덱스5의 값 50까지의 최장거리 max_len은? 50>max_value이므로, max_len++하고 max_index,max_value 업데이트... //4,5,50
# ...
# 인덱스i의 값 input[i]까지의 최장거리 max_len은?
# if input_list[i] > max_value:
#     max_len += 1
#     max_index = i
#     max_value = input_list[i]
# else:
#     continue
#
# 위의 작업을 index 0 ~ N-1까지.

for i in range(N):
    if input_list[i] > max_value:
        max_len += 1
        max_index = i
        max_value = input_list[i]
    else:
        continue
print(max_len)

# # 2차시도.....실패.....
# print("new try!!")
# input_list=[10,20,10,30,20,50,11,12,13,14,15,16] # answer = 7
# answer = 7
# N = len(input_list)
#
# max_len = 0
# max_index, max_value = 0,0
# result = [0] * N
# result_max_len = 0
#
# for i in range(N):
#     max_len = 0
#     max_index, max_value = 0,0
#     for j in range(i, N):
#         if input_list[j] > max_value:
#             max_len += 1
#             max_index = j
#             max_value = input_list[j]
#         else:
#             continue
#     result[i] = max_len
#     result_max_len = max(max_len, result_max_len)
#
#
# print(result_max_len)
# print(result)
# assert result_max_len is answer


#
# # 3차시도...과연......탈락...그냥 강의해설 본다.
#
# 새로운 구상!
# 이번엔 n개의 원소를 갖는 인풋리스트 input_list를 순차적으로 순회하면서,
# 해당 turn에서의 last_value_list[1], last_value_list[2], ....last_value_list[n-1]를 계산한다.
# (여기서 last_value_list[i]는 최장길이가 i인 subsequence의 마지막 원소를 담은 리스트다.)
#
# ex) 10, 20, 30, 50, 15, 17, 19, 20
# 10까지의 최장 후보들은
# last_value_list[1] = [10]
# 20까지의 최장 후보들은
# last_value_list[1] = [10, 20]
# last_value_list[2] = [20]     //last_value_list[1]안에 20보다 작은 수가 존재한다면, 20을 last_value_list[2]에 넣는다.
# 30까지의 최장 후보들은
# last_value_list[1] = [10, 20, 30]
# last_value_list[2] = [20, 30]
# last_value_list[3] = [30]
# 50까지의 최장 후보들은
# last_value_list[1] = [10, 20, 30,50]
# last_value_list[2] = [20, 30,50]
# last_value_list[3] = [30,50]
# last_value_list[4] = [50]
# 15까지의 최장 후보들은
# last_value_list[1] = [10, 20, 30,50,15]
# last_value_list[2] = [20, 30,50,15]
# last_value_list[3] = [30,50]
# last_value_list[4] = [50]
# 17까지의 최장 후보들은
# last_value_list[1] = [10, 20, 30,50,15,17]
# last_value_list[2] = [20, 30,50,15,17]
# last_value_list[3] = [30,50,17]
# last_value_list[4] = [50]
#
# ...
#
# input[i]까지의 최장후보들은
# last_value_list[1] = ...
# ...
# last_value_list[i+1] = ...
#
# last_value_list[]는 굳이 리스트의 리스트로 관리안해도 되겠다. 리스트의 최소값만은 관리해되 될듯 보인다.(>> min_value[max_length])

#
# 10까지의 최장후보는
# min_value[1] = 10 //최장길이가 1인 subsequence의 last원소...
# 20까지의 최장후보는
# min_value[1] = 10
# min_value[2] = 20
# 30까지의 최장후보는
# min_value[1] = 10
# min_value[2] = 20 //min_value[1]이 30보다 작으니 min_value[2] = min(30, min_value[2])
# min_value[3] = 30
# ...
# input_list[i]까지의 최장후보는
# min_value[1] = ...
# min_value[2] = ...
# ...
# min_value[i+1] = ...


# 코딩시작 .....
# input_list = [10, 20, 30, 50, 15, 17, 19, 20]
# N = len(input_list)

# N = int(input())
# input_list = list(map(int, input().split(' ')))
#
# min_value = [0] * (len(input_list) + 1)
#
# for i in range(N):
#     # print(i, min_value,input_list[i])
#     if i == 0:
#         min_value[1] = input_list[i]
#         continue
#     for j in range(1, (i+1)+1):
#         if min_value[j-1] != 0 and min_value[j-1] < input_list[i]:
#             if min_value[j] != 0:
#                 min_value[j] = min(min_value[j], input_list[i])
#             else:
#                 min_value[j] = input_list[i]
#
# # print(min_value)
# max_len = 0
# for i in range(len(min_value)):
#     if min_value[i] != 0:
#         max_len = i
# print(max_len)


#
# # 강의해설본후...직접
# D[i]를 도입해서 푼다. D[i]는 input_list[i]를 마지막원소로갖는 부분수열의 최장거리를 나타내는 배열이다.
# 또다른 대표적 다이나믹프로그래밍 문제였던 Knapsack문제처럼 테이블로 과정을 살펴보는 것처럼 구현하게 된다. (다만 Knapsack처럼 2차원배열을 사용하진 않는다)
#

# 1 좋다 우선 input값을 받자
N = int(input())
input_list = list(map(int, input().split(' ')))
# input_list = [10, 20, 10, 30, 20, 50]
# N = len(input_list)
# answer = 4

# 2 D[i]를 세팅하자. 처음엔 D[i]의 정의에 따라 모두 1로 초기화한다.
D = [1] * N

# 3 순회하면서, D[i]를 업데이트 해가자. (여기선 점화식을 그대로 코드로 옮긴다.)
for i in range(N):
    for j in range(i):
        if input_list[i] > input_list[j]:
            D[i] = max(D[i], D[j] + 1)
    # print(D)

# 4 D[i]를 완성했으니, 내부에서 가장 큰 원소를 찾아 출력하고 종료하자.
# max_distance = 0
# for data in D:
#     max_distance = max(max_distance, data)
# print(max_distance)
print(max(D))
