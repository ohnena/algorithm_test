#
# # 11.1 최소힙
# # 1927
# # easy,힙,자료구조,20분
#
#
# 문제
# 널리 잘 알려진 자료구조 중 최소 힙이라는 것이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
#
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.
#
# 입력
# 첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 2^31보다 작다.
#
# 출력
# 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
#
# 입력예
# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32
#
# 출력예
# 0
# 1
# 2
# 12345678
# 0










# # 구상 (Heap 복습전...)
# -힙을 클래스로 구현
# -class minHeap
# -멤버 root
# -__init__(),push(),pop() 정의 필요
# -근데 문득, 생각해보니 노드가 필요하겠구나. class Node.....       //Heap 복습하고 돌아오자...

# # 구상 (Heap 복습후..)
# -우선 입력된 값을 배열에 모두 넣은 후 차례로 순회하며, 값이 자연수이면 heap.insert(값)를 0이면 heap.pop()을 수행해서 출력한다.
# -작은값을 pop하기위해서 minHeap으로 구현한다.
# -만약 힙이 비어있다면 0을 출력한다.



# MinHeap 구현..   >> Pypy3로는 합격, Python3로는 시간초과 탈락.....(heapq라이브러리를 이용하여 간편하게 구현 가능 -_-...하아...)
class Heap:
    def __init__(self, data):
        # print(">> MinHeap Created...")
        self.heap_array = list()  # 파이썬의 list를 이용해서 쉽게 배열을 구현. 심지어 append()로 뒤로 차례로 넣을 수도 있음.
        self.heap_array.append(None)  # 구현을 수월하게 하기 위해 index=0은 비우고, 1부터 사용.
        self.heap_array.append(data)

    def move_up(self, inserted_index):
        if inserted_index <= 1:
            return False
        parent_index = inserted_index // 2
        if self.heap_array[inserted_index] < self.heap_array[parent_index]:
            return True
        else:
            return False

    def pop(self):
        if len(self.heap_array) <= 1:  # 힙이 비었을땐 0을 리턴...
            return 0
        min_value = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]

        inserted_index = 1
        while self.move_down(inserted_index):
            left_child_index = inserted_index * 2
            right_child_index = inserted_index * 2 + 1

            # case1 왼쪽 자식만 있을때... > 왼쪽 자식과 비교하여 swap... (굳이 비교는 안해도 되긴 할듯...)
            if right_child_index >= len(self.heap_array):
                if self.heap_array[inserted_index] > self.heap_array[left_child_index]:
                    self.heap_array[left_child_index], self.heap_array[inserted_index] = self.heap_array[
                                                                                             inserted_index], \
                                                                                         self.heap_array[
                                                                                             left_child_index]
                    inserted_index = left_child_index
            # case2 양쪽 자식 모두 있을때 ... > 왼쪽,오른쪽 자식과 모두 비교...
            else:
                if self.heap_array[left_child_index] < self.heap_array[right_child_index]:
                    if self.heap_array[inserted_index] > self.heap_array[left_child_index]:
                        self.heap_array[left_child_index], self.heap_array[inserted_index] = self.heap_array[
                                                                                                 inserted_index], \
                                                                                             self.heap_array[
                                                                                                 left_child_index]
                        inserted_index = left_child_index

                else:
                    if self.heap_array[inserted_index] > self.heap_array[right_child_index]:
                        self.heap_array[right_child_index], self.heap_array[inserted_index] = self.heap_array[
                                                                                                  inserted_index], \
                                                                                              self.heap_array[
                                                                                                  right_child_index]
                        inserted_index = right_child_index

        return min_value

    def insert(self, data):

        # 비어있을때...
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return

        # data를 배열끝에 삽입
        self.heap_array.append(data)
        inserted_index = len(self.heap_array) - 1

        # 삽입한 data의 노드를 부모와 비교하여 윗 level로 이동시키기 (반복문)
        while self.move_up(inserted_index):
            parent_index = inserted_index // 2
            self.heap_array[parent_index], self.heap_array[inserted_index] = \
                self.heap_array[inserted_index], self.heap_array[parent_index]  # Node Swapping...
            inserted_index = parent_index

    def move_down(self, inserted_index):

        if len(self.heap_array) <= 1:
            return False

        left_child_index = inserted_index * 2
        right_child_index = inserted_index * 2 + 1

        # case1 왼쪽 자식 노드도 없을때....
        if left_child_index >= len(self.heap_array):
            return False
        # case2 왼쪽 자식만 있을때... > 왼쪽 자식과 비교...
        elif right_child_index >= len(self.heap_array):
            if self.heap_array[inserted_index] > self.heap_array[left_child_index]:
                return True
        # case3 양쪽 자식 모두 있을때 ... > 왼쪽,오른쪽 자식과 모두 비교...
        else:
            if self.heap_array[left_child_index] < self.heap_array[right_child_index]:
                if self.heap_array[inserted_index] > self.heap_array[left_child_index]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[inserted_index] > self.heap_array[right_child_index]:
                    return True
                else:
                    return False

N = int(input())
input_list = []
for _ in range(N):
    input_list.append(int(input()))

heap = None
for data in input_list:
    if data == 0:
        if heap == None:
            print(0)
        else:
            print(heap.pop())
    else:
        if heap == None:
            heap = Heap(data)
        else:
            heap.insert(data)



# # heapq 라이브러리 사용법
# -heapq라이브러리를 사용하면 일반리스트를 힙처럼 사용할 수 있다
# -ex)
# import heapq
# heap = []
# heapq.heappush(heap, 5)
# heapq.heappop(heap)




# 해답 ...heapq 라이브러리 이용 -_-..... 이거도 PyPy3에서만 성공...

import heapq

n = int(input())
heap = []
result = []

for _ in range(n):
    data = int(input())
    if data == 0:
        if heap:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, data)

for data in result:
    print(data)




# * 소회
# -힙문제를 만나서 힙이라는 자료구조를 복습하는 계기가 되었다. 다행이다 (11_0 Heap.py 참고요망)
# -덕분에 복습하며 힙을 다시 새로 직접 구현해보았다. min heap, max heap 모두.
# -heap이라는 자료구조의 성질이 꽤나 흥미로웠다. 결론부터 얘기하자면 힙은 배열만으로 구현이 가능하다.
#  힙이 기본적으로 완전2진트리이기때문에 왼쪽부터 차례로 child가 추가되고,
#  그래서 index가 절묘하게 맞아 떨어지기때문이다. (어떤힙에 대해서 우하향으로 index를 읽어보면, 1 2 3 4 5 6 이런식으로 순차진행이 된다)
#  (물론 insert, pop 구현은 꽤나 까다롭긴하지만, 배열만으로 할 수 있는게 어디냐)
# -복습내용엔 힙과 2진탐색트리(BST)의 차이도 나왔다. BST는 생김새가 힙보다 한단계 더 까다롭다.
#  BST는 left child < parent <=(or <) right child 라는 조건이 있는 대신, 힙은 자식이 그냥 parent보다 작거나 크기만 하면 되기때문이다
# -이 11_1문제에선 복습한김에 직접구현해서도 제출해보았는데, 해답에선 heapq라이브러리를 이용해서 간단히 구현했더라 -_-
#  둘다 제출해보았는데, Python3에선 시간초과였고, PyPy3에선 합격했다. 아마 PyPy3가 메모리에는 조금 약하지만 속도가 더 빠르다곤했다
# -heapq라이브러리를 살펴보니, 디폴트가 mean heap구조로 되어 있더라. max heap으로 사용하고싶으면 insert,pop시에 data에 -1을 곱해서 해야한단다
#  (이게 standard한 사용법인듯...꼼수인듯보이지만)
# -결론: 어쨌든 다음부턴 힙구현시 heapq라이브러리를 사용하자 -_-...