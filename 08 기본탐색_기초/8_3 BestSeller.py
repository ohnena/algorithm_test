# 8.3 베스트셀러
# 1302
# easy, 탐색, 20분

# 입력
# 첫째 줄에 오늘 하루 동안 팔린 책의 개수 N이 주어진다. 이 값은 1,000보다 작거나 같은 자연수이다. 둘째부터 N개의 줄에 책의 제목이 입력으로 들어온다. 책의 제목의 길이는 50보다 작거나 같고, 알파벳 소문자로만 이루어져 있다.
#
# 출력
# 첫째 줄에 가장 많이 팔린 책의 제목을 출력한다. 만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.

# //input
# 5
# top
# top
# top
# top
# kimtop
#
# //output
# top





def bestSeller(input_list):
    dic = dict()
    for data in input_list:
        if data not in dic.keys():
            dic[data] = 0
        dic[data] += 1
    tuples = sorted(dic.items(), key=lambda item: (-item[1], item[0]))
    return tuples[0][0]


# <<< TEST CODE >>> START
N = 5
input_data = [
"top",
"top",
"top",
"top",
"kimtop",
"ho",
"ho",
"ho",
"ho"
]
answer = "ho"

assert bestSeller(input_data) is answer

# dic = {"ha":1, "ho":2}
# print(dic.items())
# print(dic.keys())
# print(dic.values())


# <<< TEST CODE >>> END



exit(1) # 테스트코드만 실행!!!!!!
N = int(input())
input_list = []
for _ in range(N):
    input_list.append(str(input()))
print(bestSeller(input_list))


# 소회
# - sorted()를 다중조건으로 수행하는 방법을 배웠다.
# - 간단한 dict()사용법을 배웠다.
# - 강사의 해답을 통해 max(dict.values())를 배웠다.
# - 주의!) dict.items(),dict.values(),dict.keys()는 모두 dict_items를 리턴한다. 리스트가아닌!

#
# 제출
#
# def bestSeller(input_list):
#     dic = dict()
#     for data in input_list:
#         if data not in dic.keys():
#             dic[data] = 0
#         dic[data] += 1
#     tuples = sorted(dic.items(), key=lambda item: (-item[1], item[0]))
#     return tuples[0][0]
#
# N = int(input())
# input_list = []
# for _ in range(N):
#     input_list.append(str(input()))
# print(bestSeller(input_list))
#
#






# 강사의 해답
#
# n = int(input())
# books = {}
#
# for _ in range(n):
#     book = input()
#     if book not in books:
#         books[book] = 1
#     else:
#         books[book] += 1
#
# target = max(books.values())     #dictionary를 value로 정렬하는 방법...
# array = []
# for book, number in books.items():
#     if number == target:
#         array.append(book)
#
# print(sorted(array)[0])