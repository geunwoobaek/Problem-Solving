# https://leetcode.com/problems/maximum-and-sum-of-array/
# comprehension
# 1<=numslots <=9, 1<=nums.length<=numslots
# approach1 Greedy하게 생각하기
# 어떻게..?  언제가 최적의 상황일까
# 가장 베스트 상황은 더 좋아질 수 없는 상황, 숫자가 같을떄
# 7 to slot 7, 만약 이보다 더 좋은 경우가 있을까?(X)
# Similiarty가 높을 수록 좋다
# 예를들어서 num_i, k하고 했을때 얻을 수 볼 수 있는 minimum loss는 |num_i - k| 이 된다.
# 항상 minimumloss가 작은것들끼리 매칭했을때 문제가 생길수 있는지 찾아볼까?
# 반례존재 [4,2,2,11,7,12,9,8]
# 12 = 1100, 7 = 0111, 4 = 0100, 3 = 0011
# approach2 [brute force]
# 모든 경우의 수를 다 구해보자 => 숫자를 모든 슬롯에 다 채워볼때 의 경우의 수
# m^n if m = 9,n == 18 이면 9^18 = 1.3*10^18 이므로 시간초과
# 그렇다면 어떻게 해야할까? DP
# DP[num_i][slot정보(슬롯들이 얼만큼 남아있는지)] num_(1~i)까지를 slot정보에 맞게 채웠을때의 최대값
# DP[]
# DP[n][mask] DP[n-1] ~을 통해서 DP[n][mask]를 구할 수 있다. 어떻게?
# Dp[n-1][mask에서 num_i를 k번째에서 한개 뺀 mask,(이때 k번째는 채워져 있어야한다)] + num_i & k
# DP[n][mask] = max(for k(0 -> numslots), DP[n-1, mask - (1<<k)] + num_i & k)
# timecomplexity: O(n * 2^numslots)




class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @lru_cache(None)
        def DP(i, slots_mask):
            result = 0
            if i == len(nums):
                return result
            for slot in range(1, numSlots+1):
                # 현재 slot이 2개 채워져있으면 continue 이때 3진법 사용
                b = 3 ** (slot)
                if (slots_mask // b) % 3 == 2:
                    continue
                result = max(result, DP(i+1, slots_mask + 3 ** slot) + (nums[i] & slot))
            return result
        result = DP(0, 0)
        return result

print(Solution().maximumANDSum([1,2,3,4,5,6], 3) == 9)