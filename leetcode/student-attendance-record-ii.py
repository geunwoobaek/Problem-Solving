# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# Given an integer n,
# return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.
# 1 <= n <= 10^5
# 'P': Present.
# 'A': Absent.
# 'L': Late.
#  n = 2
#  A number, P number, L number 
# cache[p_number][a_number][l_number] = number of possible attendance records
# bottomup
# cache[p_number][a_number][l_number] = max(cache[p_number-1][a_number][l_number], cache[p_number][a_number-1][l_number], cache[p_number][a_number][l_number-1])   

# 문제 P,A,L로 n개를 순열해야한다.
# 단 A는 한번만 사용가능, L은 2번까지 연속가능
# 이때 어떻게 해야하나
# 규칙성을 생각해보자
# n = 2, "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Bruteforce DFS로 백트래킹 해보기 WorstCase O(n^(10^5))
# n = 3 
# bruteforce


# p 2개, a 1개, l 2개
class Solution(object):
    def checkRecord(self, n):
        if n == 1:
            return 3
        if n == 0:
            return 0
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i-1] + nums[i-2])% 1000000007)
            i += 1
        result = (nums[n] + nums[n-1] + nums[n-2]) % 1000000007
        for i in range(n):
            result += nums[i+1] * nums[n-i] % 1000000007
            result %= 1000000007
        return result