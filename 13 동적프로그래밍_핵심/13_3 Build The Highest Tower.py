# 복습 차원에서 펜엔노트 시뮬을 해보고, 다시 코딩해본다

# D[i] = "i번째 블록을 가장 아래 두었을때의 탑의 최고높이"
# D[i] = max(D[i], D[j] + B[i].height) if B[i].area > B[j].area (0 <= j < i)
# - D는 최초 모두 0으로 초기화한다
# - B는 맨 앞에 (0,0,0,0)을 추가한다
# - B는 (번호,Area,Height,Weight)의 블록튜플의 리스트이고 Weight기준으로 정렬되어 있어야 한다

# 예상 인풋
# 5
# 25 3 4
# 4 4 6
# 9 2 3
# 16 2 5
# 1 5 2
# 예상 아웃풋
# 3
# 5
# 3
# 1

N = int(input())
B = [(0,0,0,0)]
for i in range(1, N+1):
    area, height, weight = map(int, input().split())
    B.append((i,area,height,weight))
B.sort(key= lambda data:data[3])

D = [0] * (N+1)

for i in range(N+1):
    for j in range(i):
        if B[j][1] < B[i][1]:
            D[i] = max(D[i], D[j]+B[i][2])

max_height = max(D)
i = N
result = []
while i > 0:
    if D[i] == max_height:
        max_height -= B[i][2]
        result.append(B[i][0])
    i -= 1
result.reverse()
print(len(result))
[print(i) for i in result]

exit()



# # 13_3 Build The Highest Tower


#
# 구상한 점화식
#
# D[i][j] = "j번째 블록으로 쌓기 시작한 탑에서, 마지막으로 i번째 블록을 올렸을때 탑의 최대 높이"
#
# (if B[i].area < B[last_block[j]].area and B[i].weight < B[last_block[j]].weight)
#     D[i][j] = D[i-1][j] + B[i].height
#     history[j].append(i)
#     last_block[j] = i
# (else)
#   D[i][j] = D[i-1][j]
#







# 첫시도....처음으로 스스로 풀어본 알고리즘 문제다...다이나믹프로그래밍중 LIS를 응용한거라는데, 우선 그냥 손가는대로 진행과정 구상하고 점화식만들어 풀었다.
# 1 입력값 받기

# N = 5
# B = [[25, 3, 4],  # [area,height,weight]
#      [4, 4, 6],
#      [9, 2, 3],
#      [16, 2, 5],
#      [1, 5, 2]]

N = int(input())
B=[]
for _ in range(N):
    B.append(list(map(int, input().split())))   # [area,height,weight]
# print(N)
# print(B)
# exit()

# 5
# 25 3 4
# 4 4 6
# 9 2 3
# 16 2 5
# 1 5 2


# 2 초기화 # D, history, last_block

B = [[10001, 10001, 10001]] + B
history = [[] for _ in range(N + 1)]
last_block = [0] * (N + 1)

D = [[0] * (N + 1) for _ in range(N + 1)]

# 3 점화식 적용
for i in range(1, N + 1):
    for j in range(1, i+1): # range(1, N + 1):

        if B[i][0] < B[last_block[j]][0] and B[i][2] < B[last_block[j]][2]:
            D[i][j] = D[i - 1][j] + B[i][1]
            history[j].append(i)
            last_block[j] = i
        else:
            D[i][j] = D[i - 1][j]


# 4 결과 출력후, 종료

result = D[N]
base = 0
max_height = 0
for i in range(N+1):
    if max_height < result[i]:
        max_height = result[i]
        base = i

print(len(history[base]))
while history[base]:
    print(history[base].pop())



# 강의해설을 본 후, 해답을 복사해왔다

# 1 입력값 받기
n = int(input())

array = []
array.append((0, 0, 0, 0))
for i in range(1, n + 1):
    area, height, weight = map(int, input().split())
    array.append((i, area, height, weight))

# 2 무게를 기준으로 블록의 리스트를 정렬합니다.
array.sort(key=lambda data: data[3])

# 3 점화식 계산
dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(0, i):
        if array[i][1] > array[j][1]: # 면적 비교...
            dp[i] = max(dp[i], dp[j] + array[i][2])

# 4 dp를 거꾸로 순회하며, 결과를 찾아내어 출력하고 종료한다.
max_value = max(dp)
index = n
result = []
while index != 0:
    if max_value == dp[index]:
        result.append(array[index][0])
        max_value -= array[index][2]
    index -= 1
result.reverse()

print(len(result))
[print(i) for i in result]