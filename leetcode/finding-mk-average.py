# 3 <= m <= 105
# 1 <= k*2 < m
# 1 <= num <= 105
# At most 105 calls will be made to addElement and calculateMKAverage.


from collections import deque
from sortedcontainers import SortedDict, SortedList

# 1,2,3,4,5,6,7 if m =3
# self.container = [1,2] calculateMKAverage() => -1
# self.container = [1,2,3] calculateMKAverage() => [1,2,3]
# self.container = [1,2,3,4] calculateMKAverage() => [2,3,4]
# self.container = [1,2,3,4,5] calculateMKAverage() => [3,4,5]
# 계속 누적합을 가지고 있다.
# 하나씩 들어올때마다 largest k, min k를 제외한 나머지를 더한다.
# 그리고 m - 2k 만큼 나눈다.

# if m =4, k = 1
# 합을 저장하고 있다. 1+2+3+5

# 1,2,3,5,7,4
# 1,2,3,5 => min = 1, max = 5, sum = 2+3
# 2,3,5,7 => min = 2, max = 7m sum = 3+5
# 3,5,7,4 => min = 3, max = 7, sum = 5+4

# min_heap, max_heap에 넣는다.
# 전체합을 가지고 있다가 새롭게 들어온 값과 빠지는 값을 더하고 빼서 전체합을 갱신한다.
class MKAverage:

    def __init__(self, m: int, k: int):
        self.queue = deque()
        self.container = SortedList()
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        self.queue.append(num)
        self.container.add(num)
        if len(self.queue) > self.m:
            pop_num = self.queue.popleft()
            self.container.remove(pop_num)

    def calculateMKAverage(self) -> int:
        if self.m > len(self.queue):
            return - 1
        print(self.container)
        return sum(self.container[self.k:-self.k]) // (self.m - 2 * self.k)





# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
