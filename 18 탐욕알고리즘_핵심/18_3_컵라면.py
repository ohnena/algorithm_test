# 예상인풋
# 7
# 1 6
# 1 7
# 3 2
# 3 1
# 2 4
# 2 5
# 6 1
#
#
#
#
# 5
# 3 1
# 3 1
# 3 1
# 4 100
# 4 100

# 해답...(가독성을 위해 변수명 수정)..
import heapq

n = int(input())
array = []
q = []

# 문제 정보를 입력 받은 이후에, 데드라인을 기준으로 정렬
for i in range(n):
    dead, num = map(int, input().split(' '))
    array.append((dead, num))
print(array)
array.sort()
print(array)

for dead, num in array:
    heapq.heappush(q, num)
    # 데드라인을 초과하는 경우에는 최소 원소를 제거
    if dead < len(q):
        heapq.heappop(q)

print(sum(q))


exit()
# 해답기반 직접....>>> 와...아이디어 굿이다!! >> 합격이긴한데...직관적이지가 않네...그냥 해답을 보자...
import heapq
N = int(input())
# problems = []
# deadlines = [[0] for _ in range(N+1)]
# deadlines = [0] * (N+1)
problems = []
for i in range(N):
    deadline, num = map(int, input().split())
    problems.append((deadline,num))
problems.sort(key=lambda  data:data[0])

heap_data = []
for deadline, num in problems:

    if len(heap_data) < deadline:   # sort했기때문에 >deadline인 케이스는 안나오겠지..?
        heapq.heappush(heap_data,num)
    elif len(heap_data) == deadline:
        heapq.heappush(heap_data, num)
        waste = heapq.heappop(heap_data)

print(sum(heap_data))
exit()







# 두번째 시도 >> 위의 반례를 고려... >>> 광탈....접근자체를 잘못한듯...
N = int(input())
# problems = []
# deadlines = [[0] for _ in range(N+1)]
# deadlines = [0] * (N+1)
problems = []
for i in range(N):
    deadline, num = map(int, input().split())
    # heapq.heappush(heap_data, (num,deadline))
    problems.append((deadline,num))
    # deadlines[dead] = max(deadlines[dead], num)
    # deadlines[dead].append(num)
    # problems.append((dead,num))
problems.sort(key=lambda  data:data[1],reverse=True)


# print(problems)
total_num = 0
current_time = 0
for deadline, num in problems:
    if current_time == N:
        break
    if current_time < deadline:
        total_num += num
        current_time += 1

print(total_num)










exit()
#첫시도....제출전 최적화시도 해보자... >> 광탈...

N = int(input())
# problems = []
# deadlines = [[0] for _ in range(N+1)]
deadlines = [0] * (N+1)
for i in range(N):
    dead, num = map(int, input().split())
    deadlines[dead] = max(deadlines[dead], num)
    # deadlines[dead].append(num)
    # problems.append((dead,num))



print(deadlines)
# exit()
total_num = 0
for i in range(0, N+1):
    total_num += deadlines[i]
    # deadlines[i].sort(reverse=True)
    # total_num += deadlines[i][0]
print(total_num)