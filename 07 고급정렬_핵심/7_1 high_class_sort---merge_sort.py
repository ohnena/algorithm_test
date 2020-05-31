# coding=utf-8

# 유형별문제풀이>07 고급 정렬-핵심
#
# *퀵,병합merge,힙...
#
# 7.1 수정렬하기2
# 백준온라인 2751
# easy(대중적인문제라..필수),정렬, 20분
#
# 팁) 수의 개수가 100만개이하..(헐..)이므로 시간복잡도 O(NlogN)인 정렬알고리즘을 사용해야한다.
# : 왜냐하면, 백만*log(2)백만
# = 백만*log(2)2^20 = 백만*20 = 2천만...
# (알고리즘에서의 log는 보통 log2라고..)
#
# 참고) 보통 파이썬이 1초에 2천만번 연산수행가능하다고 가정해야한다. 많이 봐줘야 5천만정도...
# : 이경우에 사용할 수 있는 O(NlogN)의 고급정렬알고리즘은 병합/퀵/힙정렬이다. 그런데 퀵정렬은 최악의경우 O(N^2)이므로 되도록이면 병합/힙정렬을 쓰라고!
# (더 간단한건 파이썬 정렬함수 쓰는게 가장 효과적...)
#
# 팁) 메모리가 허용된다면 Python3보다는 PyPy3가 더 빠르니깐, PyPy3로 제출하라고!
#
#
#
# Q. 병합정렬?
# A. 분할정복 방식이용.
#


def merge_sort(array):
    if len(array) <= 1:
        return array


    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    # print(id(left),id(right))
    # left = sorted(array[:mid])
    # right = sorted(array[mid:])
    # print(id(array), id(array[:mid]), id(array[mid:]))
    # print(left, right)

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    # print(result)
    return result


# print(merge_sort([5, 4, 3, 9, 2, 4, 6, 7, 8]))


N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))

# l = merge_sort(l)
l = sorted(l)         # 실제 시험장에선 이 코드를 사용하는게 낫겠지!...


for i in l:
    print(i)
