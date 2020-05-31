


# 해답...굉장히 심플한 아이디어인데 감탄이 나온다...와우.
# 이문제는 정렬만 하면되는 문제라고 한 이유가 있다. O(NlogN)
import sys

n = int(input())
k = int(input())

# 집중국의 개수가 n 이상일 때
if k >= n:
    print(0) # 각 센서의 위치에 설치하면 되므로 정답은 0
    sys.exit()

# 모든 센서의 위치를 입력 받아 오름차순 정렬
array = list(map(int, input().split(' ')))
array.sort()

# 각 센서 간의 거리를 계산하여 내림차순 정렬
distances = []
for i in range(1, n):
    distances.append(array[i] - array[i - 1])
distances.sort(reverse=True)

# 가장 긴 거리부터 하나씩 제거
for i in range(k - 1):
    distances[i] = 0

print(sum(distances))








exit()
# 해답기반으로 풀었다가 광탈... K>N인경우를 고려하지 못함...ㅠㅠ 아이씨..
N = int(input())
K = int(input())
# if K >= N:
#     print(0)
#     exit()
sensors = list(map(int,input().split()))
sensors.sort()
distances = [0] * (N-1)

for i in range(N-1):
    distances[i] = sensors[i+1] - sensors[i]

# print(sensors)
# print(distances)

distances.sort(reverse=True)
for i in range(K-1):
    distances[i] = 0
    # distances.pop()
# print(distances)
result = 0
for dist in distances:
    result += dist
print(result)

exit()







# 구상 >>> 역시 광탈. 논리자체가 빈약해...
# 입력받은 센서의 좌표중, max_x - min_n / K 가
# 집중국 개별로 할당받은 최대 범위라고 하고
# ... 설명하기도 어렵네 >>> 논리가 빈약하니 설명하기도 어려운듯 -_-...



N = int(input())
K = int(input())
sensors = list(map(int,input().split()))
sensors.sort()
fragment = (sensors[len(sensors)-1] - sensors[0]) / K

start = -1
end = -1
heads = []

for x in sensors:
    # if pre_x == x:
    #     continue
    # pre_x = x

    if start < 0:
        start = x
        continue

    if x - start  > fragment:
        heads.append([start,end])
        start = x
        end = x
    else:
        end = x

    if x == sensors[len(sensors)-1]:
        heads.append([start,end])


result = 0
for range in heads:
    result += range[1] - range[0]
print(result)

# 6
# 3
# 1 6 9 3 6 7
#
# 6
# 2
# 1 6 9 3 6 7





# 6
# 7
# 1 6 9 3 6 7


# 6
# 6
# 1 6 9 3 6 7