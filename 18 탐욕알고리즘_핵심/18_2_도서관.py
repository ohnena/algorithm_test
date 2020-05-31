
#해답...heapq를 이용하여 Minheap,Maxheap을 구현한게 인상적.... (하지만 내가 만든 코드가 더 심플한듯..)

import heapq

n, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
positive = []
negative = []

# 가장 거리가 먼 책까지의 거리
largest = max(max(array), - min(array))

# 최대 힙(Max Heap)을 위해 원소를 음수로 구성
for i in array:
    # 책의 위치가 양수인 경우
    if i > 0:
        heapq.heappush(positive, -i)
    # 책의 위치가 음수인 경우
    else:
        heapq.heappush(negative, i)

result = 0

while positive:
    # 한 번에 m개씩 옮길 수 있으므로 m개씩 빼내기
    result += heapq.heappop(positive)
    for _ in range(m - 1):
        if positive:
            heapq.heappop(positive)

while negative:
    # 한 번에 m개씩 옮길 수 있으므로 m개씩 빼내기
    result += heapq.heappop(negative)
    for _ in range(m - 1):
        if negative:
            heapq.heappop(negative)

# 일반적으로 왕복 거리를 계산하지만, 가장 먼 곳은 편도 거리 계산
print(-result * 2 - largest)











# 성공!!!! >> 캬~~ 그런데 해답과는 접근이 살짝 다르다...해답은 heapq를 이용하여 Minheap, Maxheap을 구현하여 만들었다..
# 입력받기
N, M = map(int, input().split())
locations = list(map(int, input().split()))

# 2개의 그룹으로 나누기...
negatives = []
positives = []
for loc in locations:
    if loc < 0:
        negatives.append(-1 * loc)
    else:
        positives.append(loc)

negatives.sort(reverse=True)
positives.sort(reverse=True)

# 가장 멀리있는 책의 위치 구하기...
max_loc = 0
if len(negatives) > 0:
    max_loc = negatives[0]
if len(positives) > 0:
    max_loc = max(max_loc, positives[0])


# 계산...(단, 가장 멀리있는 책을 가장 마지막에 가는 것으로 결정...마지막에 빼주기...)
total_steps = 0
for i in range(0, len(negatives), M):
    total_steps += negatives[i] * 2

for i in range(0, len(positives), M):
    total_steps += positives[i] * 2

total_steps -= max_loc

# 결과 출력
print(total_steps)




# 반례 생각
# 3 3
# -139 -121 -120