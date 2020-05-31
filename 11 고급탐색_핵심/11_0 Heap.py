# Ex. Max Heap
class Heap:
    def __init__(self, data):
        print(">> MaxHeap ver1 Created...")
        self.heap_array = list()  # 파이썬의 list를 이용해서 쉽게 배열을 구현. 심지어 append()로 뒤로 차례로 넣을 수도 있음.
        self.heap_array.append(None)  # 구현을 수월하게 하기 위해 index=0은 비우고, 1부터 사용.
        self.heap_array.append(data)

    def move_up(self, inserted_index):
        if inserted_index <= 1:
            return False
        parent_index = inserted_index // 2
        if self.heap_array[inserted_index] > self.heap_array[parent_index]:
            return True
        else:
            return False

    def pop(self):
        if len(self.heap_array) <= 1:  # 힙이 비었을땐 0을 리턴...
            return 0
        max_value = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]

        inserted_index = 1
        while self.move_down(inserted_index):
            left_child_index = inserted_index * 2
            right_child_index = inserted_index * 2 + 1

            max_index = inserted_index
            if left_child_index <= len(self.heap_array) - 1:
                if self.heap_array[left_child_index] > self.heap_array[max_index]:
                    max_index = left_child_index
            if right_child_index <= len(self.heap_array) - 1:
                if self.heap_array[right_child_index] > self.heap_array[max_index]:
                    max_index = right_child_index

            self.heap_array[max_index], self.heap_array[inserted_index] = self.heap_array[inserted_index], \
                                                                          self.heap_array[max_index]
            inserted_index = max_index

        return max_value

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

        max_index = inserted_index
        if left_child_index <= len(self.heap_array) - 1:
            if self.heap_array[left_child_index] > self.heap_array[max_index]:
                max_index = left_child_index
        if right_child_index <= len(self.heap_array) - 1:
            if self.heap_array[right_child_index] > self.heap_array[max_index]:
                max_index = right_child_index

        if max_index != inserted_index:
            return True
        else:
            return False


# 테스트
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

print("popped:", heap.pop(), heap.heap_array)
print("popped:", heap.pop(), heap.heap_array)
print("popped:", heap.pop(), heap.heap_array)


# Ex. Max Heap   (강의예제방식으로 move_down(), pop()을 수정...)
class Heap:
    def __init__(self, data):
        print(">> MaxHeap ver2 Created...")
        self.heap_array = list()  # 파이썬의 list를 이용해서 쉽게 배열을 구현. 심지어 append()로 뒤로 차례로 넣을 수도 있음.
        self.heap_array.append(None)  # 구현을 수월하게 하기 위해 index=0은 비우고, 1부터 사용.
        self.heap_array.append(data)

    def move_up(self, inserted_index):
        if inserted_index <= 1:
            return False
        parent_index = inserted_index // 2
        if self.heap_array[inserted_index] > self.heap_array[parent_index]:
            return True
        else:
            return False

    def pop(self):
        if len(self.heap_array) <= 1:  # 힙이 비었을땐 0을 리턴...
            return 0
        max_value = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]

        inserted_index = 1
        while self.move_down(inserted_index):
            left_child_index = inserted_index * 2
            right_child_index = inserted_index * 2 + 1

            # case1 왼쪽 자식만 있을때... > 왼쪽 자식과 비교하여 swap... (굳이 비교는 안해도 되긴 할듯...)
            if right_child_index >= len(self.heap_array):
                if self.heap_array[inserted_index] < self.heap_array[left_child_index]:
                    self.heap_array[left_child_index], self.heap_array[inserted_index] = self.heap_array[
                                                                                             inserted_index], \
                                                                                         self.heap_array[
                                                                                             left_child_index]
                    inserted_index = left_child_index
            # case2 양쪽 자식 모두 있을때 ... > 왼쪽,오른쪽 자식과 모두 비교...
            else:
                if self.heap_array[left_child_index] > self.heap_array[right_child_index]:
                    if self.heap_array[inserted_index] < self.heap_array[left_child_index]:
                        self.heap_array[left_child_index], self.heap_array[inserted_index] = self.heap_array[
                                                                                                 inserted_index], \
                                                                                             self.heap_array[
                                                                                                 left_child_index]
                        inserted_index = left_child_index

                else:
                    if self.heap_array[inserted_index] < self.heap_array[right_child_index]:
                        self.heap_array[right_child_index], self.heap_array[inserted_index] = self.heap_array[
                                                                                                  inserted_index], \
                                                                                              self.heap_array[
                                                                                                  right_child_index]
                        inserted_index = right_child_index

        return max_value

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
            if self.heap_array[inserted_index] < self.heap_array[left_child_index]:
                return True
        # case3 양쪽 자식 모두 있을때 ... > 왼쪽,오른쪽 자식과 모두 비교...
        else:
            if self.heap_array[left_child_index] > self.heap_array[right_child_index]:
                if self.heap_array[inserted_index] < self.heap_array[left_child_index]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[inserted_index] < self.heap_array[right_child_index]:
                    return True
                else:
                    return False

        #
        # # before code...
        #
        # max_index = inserted_index
        # if left_child_index <= len(self.heap_array) - 1:
        #     if self.heap_array[left_child_index] > self.heap_array[max_index]:
        #         max_index = left_child_index
        # if right_child_index <= len(self.heap_array) - 1:
        #     if self.heap_array[right_child_index] > self.heap_array[max_index]:
        #         max_index = right_child_index
        #
        # if max_index != inserted_index:
        #     return True
        # else:
        #     return False


# 테스트
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

print("popped:", heap.pop(), heap.heap_array)
print("popped:", heap.pop(), heap.heap_array)
print("popped:", heap.pop(), heap.heap_array)


# # 예상결과...
# [None, 20, 10, 15, 5, 4, 8]
# popped: 20 [None, 15, 10, 8, 5, 4]
# popped: 15 [None, 10, 5, 8, 4]
# popped: 10 [None, 8, 5, 4]


# #
# # 소회
# #
# -자료구조중 Heap을 복습했다
# -힙은 완전2진트리이다. 노드가 child를 2개이하로만 가질 수 있고, 왼쪽부터 삽입되어야 하는게 완전2진트리이다.
# -힙은 최소힙과 최대힙 2종류로 나뉜다. 최소값이나 최대값을 빠르게 얻고자할때 힙을쓴다. O(logN)이기때문이다.
# -참고로 2진탐색트리는 크기비교시 parent가 left child와 right child의 사이에 위치한다. 하지만 힙은 그런 규칙은 없다. 그냥 parent가 left,right보다 크기만하면된다.
# -특이사항은 Heap은 그냥 일반배열로 구현할 수 있다. 완전2진트리이기때문이다. (index가 절묘하게 맞아떨어짐...)
# -left_child_index = parent_index * 2
# -right_child_index = parent_index * 2 + 1
# -리스트를 멤버로 갖는 class Heap을 구현한다
# -메소드는 4가지를 구현한다. // insert(data), bool move_up(inserted_index), pop(), bool move_down(inserted_index)
# -힙의 insert매커니즘은 말단에 일단 삽입한 이후, 부모와 비교해가며 위로 스와핑을 반복해가는 것이다. 그래서 bool move_up함수 필요...
# -힙의 pop매커니즘은 root를 팝하면, root에 말단의 노드를 가져온 후, 거기서부터 자식과 비교해가며 아래로 스와핑을 반복해가는 것이다
#  그래서 bool move_down함수 필요...


# Ex. Min Heap    //최초의 Max Heap을 살짝 수정해본다...
class Heap:
    def __init__(self, data):
        print(">> MinHeap Created...")
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


# 테스트
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

print("popped:", heap.pop(), heap.heap_array)
print("popped:", heap.pop(), heap.heap_array)
print("popped:", heap.pop(), heap.heap_array)
