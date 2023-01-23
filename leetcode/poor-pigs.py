# https://leetcode.com/problems/poor-pigs/
# approach
# 1 pig process 2 bucket, 2 pigs process 4 buckets, 3 pigs process 5 buckets in oneday
# test_num = int(minutesToTest/minutesToDie)
# 이분탐색으로 pigs를 찾아보자 1<=pigs<=1000
# 한번에 피그수로 처리가능한 buckets의 수를 구해보자
# F(Pig):
#   ff Pig%2 == 0 : return (3/2)Pig
#   else: return (3/2)(Pig-1) + 1
# F(Pig)*test_num >= buckets
# F(Pig) >= buckets/test_num
# Using quadratic equation
#
class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
print(Solution().poorPigs(1000, 15, 60) == 5)