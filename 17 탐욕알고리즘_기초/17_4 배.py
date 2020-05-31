# 극악의 난이도
# 해답의 아이디어 그대로 다시 짜보았다...하아..3중 반복문이 웬말이냐...
N = int(input())
cranes = list(map(int, input().split()))
cranes.sort()#reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort()#reverse=True)
checked = [False] * M

max_cranes = max(cranes)
max_boxes = max(boxes)
if max_boxes > max_cranes:
    print(-1)
    exit()


position = [0] * len(cranes)
count = 0
time = 0
while (True):

    if count == len(boxes):
        break
    for i in range(len(cranes)):

        while position[i] < len(boxes):

            if checked[position[i]] == False and cranes[i] >= boxes[position[i]]:
                checked[position[i]] = True
                position[i] += 1 # cranse[i]가 다음으로 체크해봐야할 박스 인덱스...
                count += 1 # 옮긴 박스 숫자 카운팅...
                break
            position[i] += 1
    time += 1

print(time)

















exit()
# 광탈...해답을 보니 뭐랄까 멀티스레드의 느낌이 드는 문제다(느낌만...) 즉 혼돈의 카오스라는...
# ...내가 접근자체를 잘못했다...너무 나이브하게 봤다...

import sys
N = int(input())
krain = [0] * N

weights = list(map(int, input().split()))
weights.sort()
weight_limit = weights[len(weights) - 1]

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort()

for i in range(M):
    if boxes[i] > weight_limit:
        print(-1)
        sys.exit()

index = 0
for i in range(len(boxes)):
    for j in range(index, len(weights)):
        if boxes[i] <= weights[j]:
            krain[j] += 1
            index = j + 1
            if index == len(weights):
                index = 0
            break

max_value = 0
for value in krain:
    if value > max_value:
        max_value = value
print(max_value)

# 3
# 1 2 3
# 6
# 2 2 2 2 2 2
