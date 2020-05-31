# 9.1 공유기설치
# 2110
# medium, 이진탐색, 40분
# //이진탐색에선 보통 쉽지 않은 문제라서, 신경좀 써서 풀어라고...

# 참고로, 이진탐색은 배열에서 중간값을 구한후, 찾는값이 중간값보다 작을때는 왼쪽 배열을, 클때는 오른쪽 배열을 재귀적으로 다시 탐색하는 방식.
# 듣기엔 간단하지? 그리고 주의해야할것!) 정렬이 되어있는 배열을 대상으로 하는 알고리즘이다! 당연.


# 문제
# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (1 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
#
# 출력
# 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

# //인풋
# 5 3
# 1
# 2
# 8
# 4
# 9

# //아웃풋
# 3


# 문제이해가 안된다!!!
# 그래서, 우선 강사의 핵심아이디어 설명을 먼저보았다 -_-...
# 예를들어, 좌표상이 1,2,4,8,9 위치에 5개의 집이 놓였고 이중 세집에 공유기를 설치할건데,
# 설치해놓고 보았을때 가장인접한 공유기간의 거리가 최대가 될 수 있는 케이스를 찾아내야 하는 것이다. (구하는건 그 최대거리)
# (아마도 '인접한공유기간의 최소거리'가 모든 경우중에 가장 커야한다는 얘기아닐까? 그래야 이진탐색을 쓰는 이유가 되는 것 같다.)
# (혹자는 이분탐색이 아닌 C분탐색이어야하지 않느냐 하네...우선 이분탐색으로 풀어보고 다시 생각해보자)
# 한마디로 여기서의 이진탐색이라는게 우리가 아는 그 흔한 이진탐색의 개념이 아니다 -_-...괜히 얏봤다...






def install(input_list):

    input_list = sorted(input_list)

    result = 0
    min = input_list[1] - input_list[0]
    max = input_list[-1] - input_list[0]




    while min <= max:
        mid = (max + min) // 2
        count = 1
        value = input_list[0]
        print("---min:",min,"------mid:'", mid, "'---max:", max, "---result:", result)

        for i in range(1, len(input_list)):
            if input_list[i] - value >= mid:
                value = input_list[i]
                # print(value)
                count += 1
        if count >= C:
            result = mid
            min = mid + 1
            # print("count Good:", count)
        else:
            max = mid - 1
            # print("count Failed:", count)
        # print(min, mid, max)


    return result

# <<< TEST CODE >>> Start...
N, C = 5, 3
input_list = [1, 2, 8, 4, 9]
answer = 3

assert install(input_list) is answer
# exit()
# <<< TEST CODE >>> End...




N, C = map(int, input().split(' '))
i_list = []
for _ in range(N):
    i_list.append(int(input()))
# i_list = sorted(i_list)

print(install(i_list))







# 제출....//시간초과 OTL...
#
# def install(N, C, input_list):
#
#     input_list = sorted(input_list)
#
#     result = 0
#     min = input_list[1] - input_list[0]
#     max = input_list[-1] - input_list[0]
#
#     while min <= max:
#         mid = (max - min) // 2       <<< 틀렸다...
#         count = 1
#         value = input_list[0]
#         for i in range(1, len(input_list)):
#             if input_list[i] - value >= mid:
#                 value = input_list[i]
#                 count += 1
#         if count >= C:
#             result = mid
#             min = mid + 1
#         else:
#             max = mid - 1
#
#     return result
#
#
#
# N, C = map(int, input().split())
# i_list = []
# for _ in range(N):
#     i_list.append(int(input()))
#
# print(install(N, C, i_list))




# # 제출 >>> 성공 (해답과 비슷하니 해답은 생략...)
# def install(input_list):
#
#     input_list = sorted(input_list)
#
#     result = 0
#     min = input_list[1] - input_list[0]
#     max = input_list[-1] - input_list[0]
#
#     while min <= max:
#         mid = (max + min) // 2
#         count = 1
#         value = input_list[0]
#
#         for i in range(1, len(input_list)):
#             if input_list[i] - value >= mid:
#                 value = input_list[i]
#                 count += 1
#         if count >= C:
#             result = mid
#             min = mid + 1
#         else:
#             max = mid - 1
#
#     return result
#
# N, C = map(int, input().split(' '))
# i_list = []
# for _ in range(N):
#     i_list.append(int(input()))
#
# print(install(i_list))


# 소회
# -이진탐색이라고 해서, 그냥 절반갈라서 작으면 좌, 크면 우로 재귀적으로 재탐색 들어가는 뭐 그런 거라고 간단히 생각했는데,
#  그걸 응용하는건 정말 차원이 다른 문제구나. 여기선 범위사이의 적정값을 찾을때까지 while문을 돌리는 문제였다..
# -이문제에서 구해야하는 것은 C개만큼의 공유기를 설치했을때, 인접한 공유기사이의 최장거리 값(A)을 구하는 것이다. 표면적으로는 특정값을
#  찾는 문제는 아니라서 '탐색'이라고 부르기어렵기때문에 이진탐색을 떠올리기 쉽지 않다.
# -하지만 A의 범위를 좁혀가며 답을 찾아가는 모양새는 영낙없는 '이진탐색'의 형태다.
# -추가적으로, 이진탐색을 재귀적/반복적으로 구하는 2가지 방법이 있고 강사는 반복문을 통해서 구하는 걸 추천하더라!
# -또 추가적으로, 이진탐색을 고려해야하는 것은 애초에 데이터의 범위가 10억(1,000,000,000)이었다... 1~10억의 범위를 좁혀가면서 답을 찾아야하기때문에 Log2(10억) = 30
# 이고 그 데이터의 개수가 20만개이므로 20만*log2(10억) = 600만 연산으로 어림잡았다...(왜 이렇게 곱하는지는 아리송하다만..)

# + 약간 아리송한건 해답에서, 최초 min을 [1]-[0]로 잡더라...