from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        def _collideTime(car1, car2):
            return (car2[0] - car1[0]) / (car1[1] - car2[1])
        st = []
        n = len(cars)
        result = [-1]*n

        for i in range(n-1, -1, -1):
            p, s = cars[i]

            while st and ((s <= cars[st[-1]][-1]) or (_collideTime(cars[i], cars[st[-1]]) > result[st[-1]] > 0)):
                st.pop()
            if st:
                result[i] = _collideTime(cars[i], cars[st[-1]])
            st.append(i)
        return result
print(Solution().getCollisionTimes([[1,2],[2,1],[4,3],[7,2]]))
