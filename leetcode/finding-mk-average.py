# 3 <= m <= 105
# 1 <= k*2 < m
# 1 <= num <= 105
# At most 105 calls will be made to addElement and calculateMKAverage.


from collections import deque
from sortedcontainers import SortedDict, SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue = deque()
        self.container = SortedList()
        self.start_k_th_value = None
        self.end_k_th_value = None
        self.k_th_sum = 0
        self.end_k_sum = 0
        self.total_sum = 0

    def addElement(self, num: int) -> None:
        self.queue.append(num)
        self.total_sum += num

        if len(self.queue) == self.m:
            self.container = SortedList(list(self.queue))
            self.start_k_th_value = self.container[self.k - 1]
            self.end_k_th_value = self.container[-self.k]
            self.k_th_sum = sum(self.container[:self.k]) + sum(self.container[-self.k:])

        if len(self.queue) > self.m:
            pop_num = self.queue.popleft()
            self.total_sum -= pop_num
            pop_num_pos = self.container.bisect_left(pop_num)
            self.container.remove(pop_num)
            self.container.add(num)
            new_num_pos = self.container.bisect_left(num)

            # 왼쪽 경계
            left_boundary = self.k - 1
            # 오른쪽 경계
            right_boundary = len(self.container) - self.k

            logic = []
            ## 왼쪽 경계에서 값이 빠지고, 새로운 값도 왼쪽 경계에 들어가면 k_th_sum += num - pop_num
            if pop_num_pos <= left_boundary and new_num_pos <= left_boundary:
                self.k_th_sum += num - pop_num
                logic.append('1')
            ## 왼쪽 경계에서 값이 빠지고, 새로운 값은 왼쪽 경계에 들어가지 않으면 k_th_sum += -pop_num + self.container[self.k - 1]
            if pop_num_pos <= left_boundary and new_num_pos > left_boundary:
                self.k_th_sum += self.container[left_boundary] - pop_num
                logic.append('2')
            ## 왼쪽 경계에서 값이 빠지지 않고, 새로운 값은 왼쪽 경계에 들어가면 k_th_sum += num - self.container[self.k - 1]
            if pop_num_pos > left_boundary and new_num_pos <= left_boundary:
                self.k_th_sum += num - self.start_k_th_value
                logic.append('3')
            ## 오른쪽 경계에서 값이 빠지고, 새로운 값도 오른쪽 경계에 들어가면 k_th_sum += num - pop_num
            if pop_num_pos >= right_boundary and new_num_pos >= right_boundary:
                self.k_th_sum += num - pop_num
                logic.append('4')
            ## 오른쪽 경계에서 값이 빠지고, 새로운 값은 오른쪽 경계에 들어가지 않으면 k_th_sum += -pop_num + self.container[-self.k]
            if pop_num_pos >= right_boundary and new_num_pos < right_boundary:
                self.k_th_sum += self.container[right_boundary] - pop_num
                logic.append('5')
            ## 오른쪽 경계에서 값이 빠지지 않고, 새로운 값은 오른쪽 경계에 들어가면 k_th_sum += num - self.container[-self.k]
            if pop_num_pos < right_boundary and new_num_pos >= right_boundary:
                self.k_th_sum += num - self.end_k_th_value
                logic.append('6')

            self.start_k_th_value = self.container[left_boundary]
            self.end_k_th_value = self.container[right_boundary]
            # print(f'queue: {self.queue}, container: {self.container}, start_k_th_value: {self.start_k_th_value}, end_k_th_value: {self.end_k_th_value}, k_th_sum: {self.k_th_sum}, total_sum: {self.total_sum}, calculateMKAverage: {self.calculateMKAverage()}, logic: {logic}')



    def calculateMKAverage(self) -> int:
        if self.m > len(self.queue):
            return - 1
        return (self.total_sum - self.k_th_sum - self.end_k_sum) // (self.m - 2 * self.k)