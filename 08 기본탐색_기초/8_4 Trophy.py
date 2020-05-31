# 8.4 트로피 진열
# 1668
# easy, 탐색, 20분



# 입력
# 첫째 줄에 트로피의 개수 N (1 ≤ N ≤ 50)이 주어진다. 둘째 줄부터 N개의 줄에 왼쪽의 트로피부터 차례대로 높이가 주어진다. 트로피의 높이는 100보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 왼쪽에서 봤을 때 보이는 개수, 둘째 줄에 오른쪽에서 봤을 때 보이는 개수를 출력한다.

# 인풋
# 5
# 1
# 2
# 3
# 4
# 5

# 아웃풋
# 5
# 1

# 핵심아이디어
# -트로피개수N이 최대50이므로, 단순구현해도된다.


# 소회
# - for trophy in reversed(trophy_list): 와 같이 리스트를 reverse하여 사용하는 법을 배웠다
# - 주의 reversed(trophy_list)의 리턴값은 리스트가 아니다. list_reverseiterator object 이다. 그래서 저런식으로 사용할 수 밖에 없다...
# - 추가!) 리스트.reverse()를 하면 간단히 리버스된다 -_-...



def func(trophy_list):
    result_list = []

    result = 0
    max = 0
    for trophy in trophy_list:
        if max == 0:
            max = trophy
            result += 1
            continue
        if trophy > max:
            result += 1
            max = trophy
    result_list.append(result)

    result = 0
    max = 0
    for trophy in reversed(trophy_list):
        if max == 0:
            max = trophy
            result += 1
            continue
        if trophy > max:
            result += 1
            max = trophy
    result_list.append(result)


    return result_list


# <<< TEST CODE >>> START

input_data = [
    5,
    1,
    3,
    2,
    4,
    5
]

output_data = [
    4,
    1
]

N = input_data[0]
input_data = input_data[1:len(input_data)]

answer = func(input_data)
assert answer[0] is output_data[0]
assert answer[1] is output_data[1]

# <<< TEST CODE >>> END


N = int(input())
input_data = []
for _ in range(N):
    input_data.append(int(input()))


answer = func(input_data)
print(answer[0])
print(answer[1])








# 최종제출
#
# def func(trophy_list):
#     result_list = []
#
#     result = 0
#     max = 0
#     for trophy in trophy_list:
#         if max == 0:
#             max = trophy
#             result += 1
#             continue
#         if trophy > max:
#             result += 1
#             max = trophy
#     result_list.append(result)
#
#     result = 0
#     max = 0
#     for trophy in reversed(trophy_list):
#         if max == 0:
#             max = trophy
#             result += 1
#             continue
#         if trophy > max:
#             result += 1
#             max = trophy
#     result_list.append(result)
#
#     return result_list
#
#
# N = int(input())
# input_data = []
# for _ in range(N):
#     input_data.append(int(input()))
#
# answer = func(input_data)
# print(answer[0])
# print(answer[1])







# 강사의 해답  //역시 코드가 깔끔~~ 그래도 내가 짠거랑 비슷함...
#
# def ascending(array):
#     now = array[0]
#     result = 1
#     for i in range(1, len(array)):
#         if now < array[i]:
#             result += 1
#             now = array[i]
#     return result
#
# n = int(input())
# array = []
#
# for _ in range(n):
#     array.append(int(input()))
#
# print(ascending(array))
# array.reverse()                     # 리스트를 reverse하는 이런 간단한 방법이있다.
# print(ascending(array))