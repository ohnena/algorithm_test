# 8.1  문서검색
# 1543
# easy,탐색,20분

# 핵심아이디어
# -문서길이 2500자, 단어길이 50자가 최대이므로, 그냥 모든경우를 찾아서 체크해서 무식하게 풀어도됨. O(NM)= 2500*50으로 큰숫자가 아니다.
# -파이썬의 리스트 comprehension을 이용할것!


# print(1)
target = "ababababa" # len:9,   7+len(string) 실패 6+len(string) 성공 <= len(target
string = "aba"

def find(target, string):
    # 1 target에서 첫글자 찾기 : i
    # 2 i부터 검사하기
    # 2.1 검사성공시, 끝 index부터 첫글자 찾기
    # 2.2 검사실패시, i+1부터 다음 첫글자 찾



    length = len(string)
    start_point = 0
    end_point = 0
    find_count = 0

    # while start_point < len(target) and start_point + len(string) <= len(target):
    while start_point + len(string) <= len(target):

        if target[start_point] == string[0]:
            success = True
            for i in range(len(string)):
                if string[i] != target[start_point + i]:
                    success = False
                    break
            if success == True:
                find_count += 1
                start_point += len(string)

            else:
                start_point += 1

        else:
            start_point += 1

    return find_count




# target = str(input())
# string = str(input())
#
# print(find(target, string))




# 해답....파이썬 리스트 comprehension을 사용하니 너무 편하게 짜네 -_-...
def find_(document, word):
    start_point = 0
    find_count = 0
    while start_point <= len(document) - len(word):
        if document[start_point : start_point + len(word)] == word:
            find_count += 1
            start_point += len(word)
        else:
            start_point += 1

    return find_count



# document = "ababababa" # len:9,   7+len(string) 실패 6+len(string) 성공 <= len(target
# word = "aba"
document = str(input())
word = str(input())



print(find_(document, word))
