# 문제
# 정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.
#
# 매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 고르는 순서에 따라서 비교 횟수가 매우 달라진다. 예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면 (10+20)+(30+40) = 100번의 비교가 필요하다. 그러나 10장과 40장을 합친 뒤, 합친 50장 묶음과 20장을 합친다면 (10+40)+(50+20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.
#
# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (1≤N≤100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다.
#
# 출력
# 첫째 줄에 최소 비교 횟수를 출력한다. (21억 이하)


# 예제입력1
# 3
# 10
# 20
# 40
n = 3
input_list = [10, 20, 40]
#
# 예제출력1
# 100
answer = 100

# # 구상
# -10 20 40 50 60 이라는 새로운 입력값으로 생각해보자.
#  결과는 (10+20)+(30+40)+(70+50)+(120+60)이다.
#  매번 이전연산의 결과가 다음 덧셈연산의 피연산자로 사용된다.
#  그렇기때문에 이전연산이 최소값이어야 결과도 최소값이
# -min heap문제다. 입력값을 모두 min heap에 넣고, pop하며 계산하면 될 듯 하다 (매우 간단하게 풀릴듯...)
# -heapq라이브러리를 사용해서 구현하자
# -그런데, 마음에 걸리는건 그리디라는 키워드가 적혀있었다. 그리디 알고리즘이 뭐더라? 가장 맛있어보이는걸 먼저 먹는 거였던가?
#  뭘 어떻게 해야하지? (그냥 문제의 원리가 그냥 그리디 알고리즘기반이란 말인건 아닐까 싶다. 아닐 수도 있으니 약간 불안...)


import heapq

heap = []
# n = int(input())
# for _ in range(n):
#     heapq.heappush(heap, int(input()))



def getHeap(input_list):
    heap = []
    for data in input_list:
        heapq.heappush(heap, data)
    return heap



def sortCards(heap):
    sum_list = []
    result = 0
    pre_sum = 0
    for _ in range(len(heap)):
        popped = heapq.heappop(heap)
        pre_sum += popped
        sum_list.append(pre_sum)

    for i in range(1, len(sum_list)):
        result += sum_list[i]
    return result


def sortCards_sol(heap):
    result = 0

    while len(heap) != 1:
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        sum_value = one + two
        result += sum_value
        heapq.heappush(heap, sum_value)
    return result


# print(sortCards(getHeap(input_list)))
# print(sortCards_sol(getHeap(input_list)))
#
# exit()

# <<< TEST CODE >>> start...
# print(sortCards(getHeap([237, 360, 447, 489])))
# print(sortCards_sol(getHeap([237, 360, 447, 489])))
# exit()
# print((230+360) + ((230+360)+440) + (((230+360)+440)+480))
# print(sortCards(getHeap([230, 360, 440, 480])))
# print(sortCards_sol(getHeap([230, 360, 440, 480])))
# exit()



import random, heapq

# 난수로 input list 생성하여 두 함수의 결과 비교 >> 결과가 다르다!
for _ in range(20):
    n = random.randint(1, 4)
    input_list = []
    for _ in range(n):
        input_list.append(random.randint(1, 10))


    # print(sortCards(getHeap(input_list)) == sortCards_sol(getHeap(input_list)))
    h1 = getHeap(input_list)
    h2 = getHeap(input_list)
    h3 = getHeap(input_list)
    if sortCards(h1) != sortCards_sol(h2):
        print(h3)

# 반례 추출 완료 [5,6,7,8]

# 결과정리: sortCards(), sortCards_sol()의 차이는,
# 전자는 pre_sum을 리스트에 모두 저장해서 최종계산을 했고, 후자는 pre_sum을 그때그때 heap에 넣었다.
# 고민결과, 내가 직접 코딩한 sortCards()가 틀린 이유를 알았다. 예를 들어보자.
# 멀리서 찾을 필요도 없다. [5,6,7,8]를 보자. sortCards()에선, (5+6) + (11+7) + (18+8)로 계산을 하고 있다
# 뭔가 이상하지 않은가? 첫번째 sum을 계산한 결과인 11이 힙에 들어있는 나머지 값 7,8보다 더 크다. 문제의 의도대로라면
# 그냥 이어서 11과 7을 더하는게 아닌, 7과8을 먼저 더한후 그것을 11과 연산해야하는게 맞다.
# 이런 이유로 sortCards_sol()에선 pre_sum을 다시 heap에 넣었던 것이다.
# 문제를 너무 물로 본 내 탓이다...


# <<< TEST CODE >>> end...











# # 해답...
# import heapq
#
# n = int(input())
# heap = []
#
# for i in range(n):
#     data = int(input())
#     heapq.heappush(heap, data)
#
# result = 0
#
# while len(heap) != 1:
#     one = heapq.heappop(heap)
#     two = heapq.heappop(heap)
#     sum_value = one + two
#     result += sum_value
#     heapq.heappush(heap, sum_value)
#
# print(result)


# 회고
# -이번문제는 간단해보였는데, 난이도도 easy였고. 그런데 어김없이 삽질을 거하게 했다
#  문제에 대한 이해가 명확하지가 않았다. 풀면풀수록 자괴감이...하아
# -우선은 해답코드를 리뷰해보자. while의 조건에 len(heap) != 1인 부분이 인상적이다.
#  딱 마지막 합계값을 heap에 딱 넣었을때, while문을 멈추는 것이다...
# -11_1에서 heap을 복습하고 어느정도 이해했다고 생각했는데, 엄한데서 자신감하락..ㅠㅠ아쉽다
# 그건그렇고 PyPy3와 Python3의 속도차가 상당하다... 0.4초 대 4초면 너무 큰 차이 아닌가? 물론 메모리가 131036kb 32256kb의 차이긴한데..그래도 좀 심하다
