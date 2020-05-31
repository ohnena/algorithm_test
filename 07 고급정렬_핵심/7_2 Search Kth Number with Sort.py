# coding=utf-8
#
#
# 7.2 K번째 수
# medium, 정렬, 25분
# //7.1과 같이 많이보는 유형(빠르게 풀 수 있어야!)
# //데이터의 개수는 5백만개이고, 데이터의 범위또한 -10^9 ~ 10^9로 크다. 그래서 계수기반정렬(꼼수)를 쓸수도 없다. 그러므로 무조건 O(NlogN) 정렬알고리즘을 사용해야.
#
# 핵심아이디어
# -최대5백만개 데이터개수. 그러므로 O(NlogN)알고리즘을 사용해야...
# -(연산수를 러프하게 잡아도...5백만*로그2(백만)=1억. 다행히 시간제한이 2초. 1초에 5천만번이라는 마지노선에 부합해서 다행인것...
# -시간에 강한 PyPy3를 선택해서 제출해야.)
#
#
# 계획
# -7.1에서 구현한 merge sort를 가져와서 테스트 해본다.


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

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

    return result



N, K = map(int, input().split(' '))
array = list(map(int, input().split(' ')))

# array = merge_sort(array)
array = sorted(array)  # 실제 시험장에선 이 코드를 사용하는게 낫겠지!...

print(array[K-1])
