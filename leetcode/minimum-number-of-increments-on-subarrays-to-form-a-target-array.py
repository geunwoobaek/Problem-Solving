class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        increase_state = True
        min_height = 0
        res = 0
        # 감소하는 상태로 변경됐을때, 계산한다. res += 현재높이 - 가장 낮은 높이
        # 감소하는 상태일때는 min_height를 계속 업데이트한다.
        # 증가하는 상태로 변경됐을때는 min_height는 업데이트 하지 않는다.
        for i in range(0, n-1):
            if increase_state and target[i] > target[i+1]:
                increase_state = False
                res += target[i] - min_height

            if not increase_state:
                min_height = target[i]

            if target[i] < target[i+1]:
                increase_state = True
        if increase_state:
            res += target[-1] - min_height
        return res

    #  short solution
    def minNumberOperations(self, A):
        res = pre = 0
        for a in A:
            res += max(a - pre, 0)
            pre = a
        return res
